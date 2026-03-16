from machine import ADC, Pin, I2C
from fifo import Fifo
from piotimer import Piotimer
from time import sleep_ms
import micropython
from screen_controller import screen_controller
from graph import graph
from HRV_analyse import hrv_analyse

micropython.alloc_emergency_exception_buf(200)

from ssd1306 import SSD1306_I2C


class HeartMaster:
    def __init__(self):
        self.min = 99999999
        self.max = 0
        self.peak = 0
        self.signal = 0
        self.thresh = 0
        self.peaks = []
        self.pulses = []
        self.count = 0
        self.loops = 0
        self.continue_measuring = False
        self.fifo = Fifo(30, typecode="i")
        self.dipped = True
        self.ppg = ADC(Pin(26))
        self.median_size = 3
        self.tmr = 0
        self.mode = "pulse"  # pulse, hrv

    def adc_callback(self, ms):
        value = self.ppg.read_u16()
        self.fifo.put(value)

    def set_thresh(self):
        if self.signal > self.max:
            self.max = self.signal
        if self.signal < self.min:
            self.min = self.signal

    def calc_thresh(self):
        self.thresh = int((self.max - self.min) * 0.9 + self.min)
        self.max = 0

    def measure(self):
        if (self.count % 250 == 0):
            graph.re_scale(self.min, self.max)
            self.calc_thresh()
            self.loops += 1
            self.prev_max = 0

        self.set_thresh()

        # print("signal:",self.signal, "threshold:",self.thresh)
        if self.signal > self.thresh:
            self.peak = self.count

        if self.signal > self.thresh:
            if self.dipped:
                self.peaks.append(self.peak)
                self.dipped = False
        if self.signal <= self.thresh:
            self.dipped = True

        self.count += 1

    def get_heart_rates(self):
        hr = []
        average_time = 0
        for i in range(0, len(self.peaks) - 1):
            time = ((1 / 250) * (self.peaks[i + 1] - self.peaks[i]))
            hr.append(int(60 / time))

        heart_rates = []
        median = hr[int(len(hr) / 2)]

        for i in range(len(hr)):
            # median boundaries
            size = self.median_size
            start = i
            end = min(len(hr), i + size)
            if end < i + size:
                diff = i + size - end
                start = i - diff

            # segment
            window = hr[start:end]

            # median
            sorted_window = sorted(window)
            window_size = len(sorted_window)

            heart_rates.append(int(sorted_window[window_size // 2]))

        heart_rate = heart_rates[0]
        if heart_rate > 240 or heart_rate < 40:
            return 0
        return heart_rate

    def get_pulses(self):
        return self.pulses

    def start_measuring_hrv(self):
        self.start_measuring_heart_rate(mode="hrv")

    # Begins a loop that measures BPM
    def start_measuring_heart_rate(self, mode="pulse"):
        self.tmr = Piotimer(period=4, mode=Piotimer.PERIODIC, callback=self.adc_callback)
        self.mode = mode
        self.continue_measuring = True
        # So long as continue_measuring is True, the loop keeps going
        while self.continue_measuring:
            # Make sure we get all data from the fifo
            while self.fifo.has_data():
                # Get ADC signal from fifo
                self.signal = self.fifo.get()
                # Display signal as graph
                graph.signal = self.signal
                graph.draw()
                # Use the signal to measure a peak
                self.measure()

            screen_controller.show()

            # When median size peaks have been measured, it's time to display a median
            if len(self.peaks) > self.median_size - 1:
                # Measure median heart rate from the given peaks
                pulse = self.get_heart_rates()
                # If the pulse has been flagged as "non-human", print a warning
                # screen_controller.fill(0)
                if pulse == 0:
                    text = "CALIBRATING..."
                    screen_controller.htext(text, 0)
                else:
                    text = f"BPM {pulse}"
                    # Center the text
                    screen_controller.htext(text, 0)
                    if mode == "hrv":
                        self.pulses.append(pulse)
                        if len(self.pulses) > 14:
                            self.stop_measuring_heart_rate()

                # Reset the peaks for the next pulse
                self.peaks = []
                screen_controller.show()

    def stop_measuring_heart_rate(self):
        if self.continue_measuring:
            self.tmr.__del__()
            self.continue_measuring = False

            if self.mode == "hrv":
                print(self.get_pulses())
                hrv_analyse.set_values(self.get_pulses())
                self.pulses = []


heart_master = HeartMaster()
# heart_master.start_measuring_heart_rate()



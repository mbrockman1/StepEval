from kivy.properties import (ObjectProperty, StringProperty)
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock
from kivy.clock import Clock
from plyer.utils import platform
from plyer import pedometer, accelerometer
from datetime import datetime
import traceback


class PedometerInterface(Widget):
    def __init__(self):
        super(PedometerInterface, self).__init__()
        self.sensorAccelerometerEnabled = False
        self.sensorPedometerEnabled = False
        self.data = {"step": None,
                     "distance": None,
                     "x_label": None,
                     "y_label": None,
                     "z_label": None}

        self.add_widget(Button(font_size='10sp',
                               size=(Window.size[0],
                                     Window.size[1] / 4),
                               pos=(Window.size[0] * .0,
                                    Window.size[1] * 0.75),
                               text="Toggle Pedometer",
                               on_release=self.pedometer_toggle))

        self.add_widget(Button(font_size='10sp',
                               size=(Window.size[0],
                                     Window.size[1] / 4),
                               pos=(Window.size[0] * .0,
                                    Window.size[1] * .5),
                               text="Toggle Accelerometry",
                               on_release=self.accelerometer_toggle))

        self.data_label = Label(
            font_size='10sp',
            size=(Window.size[0],
                  Window.size[1] * .5),
            pos=(0, 0),
            text=("Timestamp: %s\nSteps: %s\nDistance: %s\nX: %s\nY: %s\nZ: %s" %
                  (datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),
                   self.data['step'], self.data['distance'],
                   self.data['x_label'], self.data['y_label'],
                   self.data['z_label'])))
        self.add_widget(self.data_label)

        self.label_maker()

    def label_maker(self):
        Clock.schedule_interval(self.label_updater, 1 / 20.)

    def label_updater(self, dt):
        self.data_label.text = (
            "Timestamp: %s\nSteps: %s\nDistance: %s\nX: %s\nY: %s\nZ: %s" %
            (datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),
             self.data['step'], self.data['distance'],
             self.data['x_label'], self.data['y_label'],
             self.data['z_label']))

    def pedometer_toggle(self, touch):
        try:
            if not self.sensorPedometerEnabled:
                pedometer.enable()
                Clock.schedule_interval(self.get_pedometer, 1 / 20.)
                self.sensorPedometerEnabled = True
            else:
                pedometer.disable()
                Clock.unschedule(self.get_pedometer)
                self.sensorPedometerEnabled = False
        except NotImplementedError:
            traceback.print_exc()
            status = "Pedometer is not implemented for your platform"

    def get_pedometer(self, dt):
        val = pedometer.count[:2]
        if not val == (None, None):
            self.data['step'] = val[0]
            self.data['distance'] = val[1]

    def accelerometer_toggle(self, touch):
        try:
            if not self.sensorAccelerometerEnabled:
                accelerometer.enable()
                Clock.schedule_interval(self.get_acceleration, 1 / 20.)
                self.sensorAccelerometerEnabled = True
            else:
                accelerometer.disable()
                Clock.unschedule(self.get_acceleration)
                self.sensorAccelerometerEnabled = False
        except NotImplementedError:
            traceback.print_exc()
            status = "Accelerometer is not implemented for your platform"
            self.ids.accel_status.text = status

    def get_acceleration(self, dt):
        val = accelerometer.acceleration[:3]
        if not val == (None, None, None):
            self.data['x_label'] = val[0]
            self.data['y_label'] = val[1]
            self.data['z_label'] = val[2]


class PedometerApp(App):

    def build(self):
        return PedometerInterface()

    def on_pause(self):
        return True


if __name__ == "__main__":
    PedometerApp().run()

#!/usr/bin/python

import tempfile
import glob

import notify2


class Main:
    def __init__(self, CRITICAL_BATTERY, LOW_BATTERY, MAX_BATTERY=100) -> None:
        self.base_bat_path = "/sys/class/power_supply/BAT0"
        self.base_tmp_path = "/tmp"
        self.error_log_path = "/var/log/battery-notify/errors.log"

        self.bat_percent_path = f"{self.base_bat_path}/capacity"
        self.bat_stat_path = f"{self.base_bat_path}/status"
        self.bat_energy_now = f"{self.base_bat_path}/energy_now"
        self.bat_energy_full = f"{self.base_bat_path}/energy_full"

        self.CRITICAL_BATTERY = CRITICAL_BATTERY
        self.LOW_BATTERY = LOW_BATTERY
        self.MAX_BATTERY = MAX_BATTERY

    def read_file(self, path):
        with open(path, "r") as opened_file:
            return opened_file.read()

    def get_percent(self) -> int:
        """
        gets current percent of battery
        """
        with open(self.bat_percent_path, "r") as percent_file:
            return int(percent_file.read())

    def get_stat(self) -> str:
        """
        gets if battery is Charging or Discharging
        """
        with open(self.bat_stat_path) as stat_file:
            return str(stat_file.read().replace("\n", ""))

    def read_notification_status(self) -> int:
        """
        reads from /tmp file to which later decides if a notification should be sent
        reading only ints for simplicity and because strings did not work
        1 = full
        2 = low
        3 = critical
        0 = none
        """
        try:
            with open(glob.glob(f"{self.base_tmp_path}/battery-state-stat.*")[0], 'r+') as notification_status:
                try:
                    return_val = int(notification_status.read())
                    notification_status.seek(0)
                except ValueError:
                    return_val = 0
        except IndexError:
            with tempfile.NamedTemporaryFile(mode='r+', delete=False, prefix="battery-state-stat.") as notification_status:
                try:
                    return_val = int(notification_status.read())
                    notification_status.seek(0)
                except ValueError:
                    return_val = 0

        return return_val

    def write_notification_status(self, status: str) -> None:
        """
        writes which notifications has been sent to a /tmp file
        reading only ints for simplicity and because strings did not work
        1 = full
        2 = low
        3 = critical
        0 = none
        """
        # below code assumes read_notification_status was already ran
        # creating battery-state-stat file
        with open(glob.glob(f"{self.base_tmp_path}/battery-state-stat.*")[0], 'r+') as notification_status:
            notification_status.truncate()
            notification_status.write(status)

    def write_logs(self) -> None:
        """
        to be ran when encountring erros and write its logs
        """
        pass

    def create_notifications(self, notif_title, notif_body, time, urgency, icon=""):
        rtrn_notif = notify2.Notification(notif_title, notif_body, icon)
        rtrn_notif.set_timeout(time)
        rtrn_notif.set_urgency(urgency)
        return rtrn_notif

    def main(self, icon: bool) -> None:
        NOTIFY_STAT = self.read_notification_status()
        BAT_STAT = str(self.read_file(self.bat_stat_path)).replace("\n", "")
        BAT_PERCENT = int(self.read_file(self.bat_percent_path))
        BAT_ENG_NOW = int(self.read_file(self.bat_energy_now))
        BAT_ENG_FULL = int(self.read_file(self.bat_energy_full))

        if BAT_STAT == "Discharging":
            if self.CRITICAL_BATTERY >= BAT_PERCENT and NOTIFY_STAT != 3:
                if icon:
                    notification = self.create_notifications(
                            "Critical Battery",
                            f"Battery Level Is {BAT_PERCENT}%",
                            15000,
                            notify2.URGENCY_CRITICAL,
                            "/usr/share/icons/Papirus/16x16/status/package-remove.svg")
                else:
                    notification = self.create_notifications(
                            "Critical Battery",
                            f"Battery Level Is {BAT_PERCENT}%",
                            15000,
                            notify2.URGENCY_CRITICAL,)

                notification.show()
                self.write_notification_status("3")

            elif self.LOW_BATTERY >= BAT_PERCENT and NOTIFY_STAT != 2:
                if icon:
                    notification = self.create_notifications(
                            "Low Battery",
                            f"Battery Level Is {BAT_PERCENT}%",
                            15000,
                            notify2.URGENCY_NORMAL,
                            "/usr/share/icons/Papirus/16x16/status/package-remove.svg")
                else:
                    notification = self.create_notifications(
                            "Low Battery",
                            f"Battery Level Is {BAT_PERCENT}%",
                            15000,
                            notify2.URGENCY_NORMAL)

                notification.show()
                self.write_notification_status("2")

            elif BAT_ENG_NOW >= BAT_ENG_FULL and NOTIFY_STAT != 1:
                if icon:
                    notification = self.create_notifications(
                            "Full Battery",
                            "Battery Level Is 100%",
                            15000,
                            notify2.URGENCY_LOW,
                            "/usr/share/icons/Papirus/16x16/status/package-install.svg")
                else:
                    notification = self.create_notifications(
                            "Full Battery",
                            "Battery Level Is 100%",
                            15000,
                            notify2.URGENCY_LOW)

                notification.show()
                self.write_notification_status("1")

        else:
            if BAT_ENG_NOW >= BAT_ENG_FULL and NOTIFY_STAT != 1:
                if icon:
                    notification = self.create_notifications(
                            "Full Battery",
                            "Battery Level Is 100%",
                            15000,
                            notify2.URGENCY_LOW,
                            "/usr/share/icons/Papirus/16x16/status/package-install.svg")
                else:
                    notification = self.create_notifications(
                            "Full Battery",
                            "Battery Level Is 100%",
                            15000,
                            notify2.URGENCY_LOW)

                notification.show()
                self.write_notification_status("1")


if __name__ == "__main__":
    notify2.init("battery-notify")
    start = Main(5, 15, 94)
    start.main(True)

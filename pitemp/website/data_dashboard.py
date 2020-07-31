class DataDashboard:
    """class to get queryset and return  information needed by template (charjs)
    example : average of temperatures on last 4 hours"""

    def __init__(self):
        self.message_to_display = str()
        self.list_temp = []
        self.list_hours = []
        self.average = float()
        self.last_update_hour = str()

    def get_average_temperature_4_hours(self, queryset):
        """Average of 4 last temperatures"""
        list_temp = []
        number = 0
        if len(queryset) >= 4:
            for i in queryset[:4]:
                list_temp.append(i.temperature)

            for temp in list_temp:
                number = temp + number
            average = number / 4
            self.average = str(average) + "°C"
        else:
            return "Vide"

    def get_information_for_chartjs(self, queryset):
        """Get data from queryset and put informations into list for ChartJS"""
        if queryset.first():  # check if queryset is empty or not
            for i in queryset:
                date = str(i.date)
                date = date[11:13] + 'h'  # change 19:12:20 to 19h
                self.list_temp.append(i.temperature)
                self.list_hours.append(date)
        else:
            self.message_to_display = 'Pas d''informations à afficher'
        self.list_temp.reverse(), self.list_hours.reverse()

    def get_last_hour_update(self, queryset):
        """Get the hour of last temperature receive"""
        if queryset.first():  # check if queryset is empty or not
            for i in queryset[:1]:
                date = str(i.date)
                date = date[11:16] + 'h'  # change 19:12:20 to 19h
                self.last_update_hour = date
        else:
            self.last_update_hour = 'Vide'

    def get_all_information_for_dashboard(self, queryset):
        """execute of all methods in class"""
        self.get_information_for_chartjs(queryset)
        self.get_average_temperature_4_hours(queryset)
        self.get_last_hour_update(queryset)



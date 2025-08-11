class DateTime:
    def print_date_time(date_time):
        dt = (date_time.timetuple())[:6]
        tt = f"{dt[0]}/{dt[1]}/{dt[2]} {dt[3]}:{dt[4]}:{dt[5]}"
        return tt

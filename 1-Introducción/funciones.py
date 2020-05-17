def salary_week(hrs, salary_hr, job):
    salary = hrs * salary_hr
    salary = salary * 7
    print("El sueldo de un", job, "es", salary)

salary_week(7, 30, "Doctor")

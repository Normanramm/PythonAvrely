from datetime import date

# Исходные данные
start = date(2014, 4, 29)
end = date(2026, 5, 9)

# Периоды с особыми коэффициентами
p1_start = date(2021, 5, 22)
p1_end = date(2021, 12, 29)  # 1 месяц за 3
coef_p1 = 3

p2_start = date(2023, 2, 11)
p2_end = date(2023, 3, 7)    # 1 день за 3
coef_p2 = 3

# Общий календарный срок (включительно)
total_days = (end - start).days + 1

# Дни в специальных периодах
p1_days = (p1_end - p1_start).days + 1
p2_days = (p2_end - p2_start).days + 1

# Базовый коэффициент для остального срока: месяц за полтора (1.5)
base_coef = 1.5

# Льготные эквиваленты по периодам
p1_equiv_days = p1_days * coef_p1
p2_equiv_days = p2_days * coef_p2
rest_days = total_days - p1_days - p2_days
rest_equiv_days = rest_days * base_coef

total_equiv_days = rest_equiv_days + p1_equiv_days + p2_equiv_days

# Перевод дней в формат «лет, месяцев, дней» (григорианский: 365/30)


def to_ymd(days: float):
    # Округляем до целого дня вниз для вывода лет/месяцев/дней
    d = int(days)
    years = d // 365
    rem = d % 365
    months = rem // 30
    days_rem = rem % 30
    return years, months, days_rem, d


cal_y, cal_m, cal_d, _ = to_ymd(total_days)
lev_y, lev_m, lev_d, lev_total_int = to_ymd(total_equiv_days)

print(
    f"Календарных: {total_days} дней = {cal_y} лет {cal_m} месяцев {cal_d} дней")
print(f"Льготных: {total_equiv_days:.0f} дней ≈ {lev_total_int} дней = {lev_y} лет {lev_m} месяцев {lev_d} дней")
print(f"Периоды: общий {total_days} дн; база (коэф. {base_coef}) {rest_days} дн → {rest_equiv_days:.0f} дн; p1 {p1_days} дн (коэф. {coef_p1}) → {p1_equiv_days} дн; p2 {p2_days} дн (коэф. {coef_p2}) → {p2_equiv_days} дн")

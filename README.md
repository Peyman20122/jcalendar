# Jalali Calendar with "Moon in Scorpio" Highlighting

This project provides functions to display the Jalali (Solar Hijri) calendar and highlight days when (according to a simplified empirical formula) the Moon is assumed to be in the constellation Scorpio. Highlighted days are shown in red.

## Features
- Display the current month or any specific Jalali month.
- Identify days when the Moon is in Scorpio (approximate formula).
- Print the calendar with Scorpio days in red.
- Search for Scorpio days within a range of Gregorian years.

## Requirements (Installation)

Before running, install the required libraries:

```bash
pip install jdatetime numpy hijri-converter gregorian
```

Note: gregorian might be available via pip install gregorian. hijri-converter is used for Gregorian to Hijri conversion.

Usage

Save the code in a Python file (e.g., persian_calendar.py) and call its functions.

1. Show current month calendar

```python
import jcalender 

jcalender.Jalali_Calender()
```

2. Show a specific Jalali month

```python
jcalender.Jalali_Calender(your_year=1403, your_month=6)  # Shahrivar 1403
```

3. Show calendar with Scorpio days highlighted

```python
jcalender.Moon_in_Scorpio_Calender()  # current month
jcalender.Moon_in_Scorpio_Calender(your_year=1403, your_month=6)  # specific month
```

4. Search for Scorpio days across two consecutive Gregorian years

```python
jcalender.Moon_in_Scorpio_Calender(Gregorian_year_1=2026, Gregorian_year_2=2027)
```

Note: your_year/your_month and Gregorian_year_1/Gregorian_year_2 are not used together.



**Main Functions**

Function Description Jalali_Calender(your_year, your_month) Prints the Jalali calendar week by week (Sat to Fri).
Moon_in_Scorpio() Returns whether the Moon is in Scorpio for the current day.
Moon_in_Scorpio_Choose_day(day, month, year) Checks a specific Gregorian date.
Moon_in_Scorpio_Calender(...) Prints the Jalali calendar with Scorpio days highlighted in red.
Mooon_is(months, years, mons) Returns a list of Scorpio days in a given Gregorian month (internal).

The "Moon in Scorpio" Formula

The formula used is empirical and not astronomically accurate – it's just a demonstration. For real calculations, use libraries like ephem or astropy.

Current formula:

```
total = (Hijri_day × 12.2) + (Jalali_day + 1)
result = (total / 30) + Jalali_month
If result is between 7.60 and 8.98 → Moon in Scorpio
```

Limitations & Known Issues

· The Scorpio formula is very crude; do not use for serious astronomical purposes.
· Moon_in_Scorpio_Calender for two Gregorian years only checks months 1–4 of the second year (possible bug).
· Colored output uses ANSI codes; may not work in all terminals/IDEs.

Sample Output

```
     Shahrivar 1403     
Sa Su Mo Tu We Th Fr
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

(Red numbers indicate Scorpio days)

**License**

This project is for educational purposes. Use the Scorpio formula with caution.

**Contributions**

Improvements (bug fixes, real astronomical calculations) are welcome.


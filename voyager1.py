days_int = int(input("Number of days after 9/25/09: "))

miles_on_day_int = 16637000000
miles_from_sun_int = miles_on_day_int + (days_int * 38241 * 24)
kilometers_from_sun_int = miles_from_sun_int * 1.609344
au_from_sun_int = miles_from_sun_int / 92955887.6

print("Miles from the sun: ", round(miles_from_sun_int))
print("Kilometers from the sun: ", round(kilometers_from_sun_int))
print("AU from the sun: ", round(au_from_sun_int))
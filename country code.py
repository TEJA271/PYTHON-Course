country_code = {'INDIA' : '0091',
                'America' : '0069',
                'Australia': '4200'}

print("country code for India - ")
print(country_code.get('INDIA' , 'not found'))

print("country code for Japan - ")
print(country_code.get('Japan' , 'not found'))
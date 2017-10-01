import random
def main():
    country_capital_dict = {"Slovenia ": "Ljubljana", "Croatia":  "Zagreb", "Austria": "Vienna","Italy": "Rome","Serbia": "Belgrade","Hungary": "Budapest","Slovakia": "Bratislava","Germany":"Berlin","France": "Paris", "Spain": "Madrid", "Portugal": "Lisbon", "England": "London","Netherlands":"Amsterdam", "Belgium": "Brussels","Bulgaria": "Sofia","Cyprus": "Nicosia","Albania":"Tirana","Andorra": "Andorra la Vella","Armenia": "Yerevan","Azerbaijan": "Baku","Belarus": "Minsk","Bosnia and Herzegovina": "Sarajevo","Czech Republic": "Prague","Denmark": "Copenhagen","Estonia": "Tallinn", "Finland": "Helsinki","Georgia":"Tbilisi","Greece": "Athens","Iceland": "Reykjavik", "Ireland": "Dublin","Kazahstan": "Astana","Latvia": "Riga", "Lichtenstein": "Vaduz","Lithuania": "Vilnius","Luxembourg":"Luxembourg"," Macedonia":"Skopje","Malta": "Valletta","Moldova":"Chisinau","Monaco":"Monaco","Montenegro": "Podgorica", "Norway": "Oslo","Poland": "Warsaw","Romania": "Bucharest", "Russia":"Moscow", "San Marino":"San Marino","Sweden":"Stockholm","Switzerland":"Bern","Turkey": "Ankara","Vatican City": "Vatican City","Ukraine": "Kiev"}


    while True:
        random_num = random.randint(0, len(country_capital_dict) -1)
        country = country_capital_dict.keys()[random_num]

        guess = raw_input("The capital of " + country + " is:")

        if check_guess(guess, country, country_capital_dict):
            print "Congrats"
        else:
            print "Wrong"

        finish = raw_input("Do you wanna continue?") .lower()

        if finish == "no":
            break
''''
    for country in country_capital_dict:
        guess=raw_input("The capital of "+  country  +" is:" )

        if   check_guess(guess,country,country_capital_dict):
            print "Congrats"
        else:
            print "Wrong"

'''

def check_guess(guess,country,country_capital_dict):
    if guess == country_capital_dict[country]:
       return True
    else:
        False


if __name__ == "__main__":
    main()


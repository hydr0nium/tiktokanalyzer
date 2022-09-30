from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.utils import ChromeType
from bs4 import BeautifulSoup
from os import system as sys, name as os_name, path as os_path
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

Stats = dict[tuple]

## TODO: Add readme extern, Add readme intern
query_restriction = 50
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def query_names(usernames: str) -> Stats:
    ret = {}
    user_list = usernames.split(",")
    count = len(user_list)
    if (len(user_list)>50):
        count = 50
        print("Es wurden mehr usernames angegeben als die maximale Suchanzahl (50).")
        print("Es werden nur die ersten 50 Einträge abgearbeitet")
        
    driver = get_driver()
    if (driver==None):
        print("Keinen unterstützten Browser Driver gefunden. Programm wird beendet...")
        input()
        exit()  
    for i in range(count):
        account = "@" + user_list[i]
        driver.get("https://www.tiktok.com/" + account)
        html = driver.page_source
        parsed = BeautifulSoup(html, 'html.parser')
        try:
            follower = parsed.find_all(attrs={"title":"Follower"})[0].text
            likes = parsed.find_all(attrs={"title":" Likes"})[0].text
        except:
            follower = None
            likes = None
        ret[account] = (follower,likes)
    return ret

def get_driver():
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service,options=options)
    except:
        try:
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service,options=options)
        except:
            try:
                service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
                driver = webdriver.Chrome(service=service,options=options)
            except:
                service = Service(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service,options=options)
    return driver

def in_json(stats: Stats) -> str:
    ret = {}
    for name,val in stats.items():
        ret[name] = {'follower':val[0], 'likes':val[1]}
    return str(ret)

def in_csv(stats: Stats) -> str:
    ret = "Username,Follower,Likes\n"
    for username,values in stats.items():
        ret = ret + str(username) + "," + str(values[0]) + "," + str(values[1]) + "\n"
    return ret

def print_start():
    pass

def clear_terminal():
    sys('cls' if os_name=='nt' else 'clear')
    
def get_input(input_name: str):
    clear_terminal()
    try:
        f = open(input_name, 'r')
    except:
      print("Die Datei konnte nicht gefunden werden!")
      i = input("Anderen Dateiname eingeben: ")
      f = get_input(i)
    return f

def main():
    print("JSON (1)")
    print("CSV (2)")
    print("Nur Ausgabe (3)")
    typ_output = int(input("Wählen sie einen Ausgabetyp aus und drücke sie enter: "))
    clear_terminal()
    output_name = ""
    if(typ_output<3 and typ_output>0):
        print("Achtung: Falls die Datei schon existiert wird diese überschrieben!")
        output_name = input("Geben sie den Name Ausgabenamen an (ohne Dateiendung): ")
        if(output_name == ""):
            output_name == "ausgabe"
        clear_terminal()
    print("Datei (1)")
    print("Manuelle Eingabe (2)")
    typ_input = int(input("Wählen sie einen Eingabetyp und drücken sie enter: "))
    clear_terminal()
    
    usernames = ""
    if(typ_input==1):
        input_name = input("Geben sie den Name der auszugebenen Datei (mit Dateiendung) an: ")
        fd = get_input(input_name)
        usernames = fd.read()
        fd.close()
    elif (typ_input==2):
        usernames = input("Bitte geben sie eine mit Komma getrennte Liste an (ohne @ und ohne Leerzeichen):\n")
      
    clear_terminal()
    print("Daten werden erfasst! (Bitte warten. Der Prozess könnte einige Minuten dauern)") 
    data = query_names(usernames) 
    if (typ_output==1):
        with open(output_name + ".JSON", 'w') as fd_json:       
            fd_json.write(in_json(data))
            print("Datei wurde erfolgreich geschrieben drücken sie Enter zum Beenden.")
            fd_json.close()
            input()
    elif (typ_output==2):
        with open(output_name + ".csv", 'w') as fd_csv:
            fd_csv.write(in_csv(data))
            print("Datei wurde erfolgreich geschrieben drücken sie Enter zum Beenden.")
            fd_csv.close()
            input()
    elif (typ_output==3):
        print("Format => USERNAME: (FOLLOWER, LIKES)")
        pprint(data)
        print("Daten erfolgreich ausgegeben drücken sie Enter zum Beenden.")
        input()
main()
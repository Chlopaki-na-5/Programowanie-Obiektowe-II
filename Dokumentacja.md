# **Programowanie obiektowe**

## Temat: Symulator automatu biletowego

**Członkowie zespołu:**

Rafał Majchrowicz

Mirosław Jachowicz

Jakub Nykiel

Damian Zawisza

## Etap I:

### **1.Wstępny opis działania programu.**

Aplikacja ma za zadanie symulować działanie automatu biletowego wzorowanego na automatach MPK. Użytkownik powinien mieć wybór wybrania biletu, a następnie możliwość zapłaty monetami i gotówką o różnym nominale. Gdy nastąpi poprawna zapłata (ilość gotówki wrzuconej przekroczy cenę biletów) automat powinien wydać resztę wraz z biletem. Jeśli nie zostanie wrzucona gotówka przez określny czas (np. minutę), automat powinien wrócić do stanu startowego oraz oddać wrzuconą gotówkę, jeśli taka była.

### **2. Analiza MoSCoW.**

**Must have:**

- Wybór biletu: Użytkownik powinien móc wybrać rodzaj biletu spośród dostępnych opcji.
- Akceptacja monet i banknotów: Automat powinien akceptować monety i banknoty o różnych nominałach jako formę płatności.
- Wydawanie biletów: Po poprawnej zapłacie automat powinien wydać bilet.
- Wydawanie reszty: Jeśli wrzucona kwota przekroczy cenę biletu, automat powinien wydać resztę.

**Should have:**

- Obsługa błędnych wpłat: Automat powinien reagować na błędne wpłaty, informując użytkownika o konieczności wrzucenia odpowiedniej kwoty.
- Wyświetlanie ceny biletu: Przed dokonaniem płatności automat powinien wyświetlić użytkownikowi cenę wybranego biletu.
- Powrót wrzuconej gotówki: Jeśli użytkownik zrezygnuje z zakupu biletu, automat powinien zwrócić wrzucone pieniądze.

**Could have:**

- Obsługa płatności bezgotówkowych: Dodanie opcji płatności kartą lub przez aplikację mobilną.

**Won't have:**

- Integracja z systemem zarządzania MPK: Rozbudowa aplikacji o możliwość sprawdzania rozkładów jazdy czy zakupu biletów okresowych.
- Obsługa karty miejskiej: Możliwość sprawdzenia aktualnego statusu.

### **3. Diagram przypadków użycia wraz ze szczegółowym opisem.**

```mermaid
flowchart LR
    subgraph 'System'
    uc1((Wybór rodzaju biletu))
    uc2((Wydanie reszty))
    uc3((Wydanie biletu))
    uc4((Wyświetlenie informacji o braku wystarczającej kwoty))
	uc5((Wyświetlenie informacji o powodzeniu transakcji))
    uc6((Wyświetlenie informacji o niepowodzeniu transakcji))
    uc7((Zakończenie transakcji po minucie bezczynności))
    uc8((Wyświetlenie dostępnych rodzajów biletów i ich cen))
    uc9((Włożenie monet/banknotów))
    uc10((Wyświetlenie aktualnej sumy zapłaconej kwoty))
    uc11((Sprawdzenie, czy suma zapłaconej kwoty przekracza cenę biletu))
    uc12((Obliczenie reszty do wydania))
    uc13((Zatwierdzenie kwoty))
    end
    customer[Użytkownik🙎‍♂️]
    customer----->uc8
    uc8 -. extend .-> uc1
    uc1 -. include .-> uc10
    uc10 -. extend .-> uc9
    uc10 -. include .-> uc13
    uc13 -. extend .-> uc11
    uc11 -. extend .-> uc4
    uc11 -. extend .-> uc12
    uc12 -. extend .-> uc2
    uc12 -. include .-> uc3
    uc3 -. include .-> uc5
    uc10 -. extend .-> uc7
    uc7 -. include.-> uc6
```
#### **Opis przypadków użycia:**  
**Nazwa przypadku:** Wyświetlenie dostępnych rodzajów biletów i ich cen  
**Aktor:** Użytkownik  
**Wyzwalacz:** Uruchomienie aplikacji  
**Scenariusz główny:**  
**1.** System wyświetla aktorowi ekran startowy zawierający informacje o rodzaju oraz cenie biletów  

**Nazwa przypadku:** Wybór rodzaju biletu  
**Aktor:** Użytkownik  
**Wyzwalacz:** Naciśniecie przycisku znajdującego się obok wybranego biletu  
**Scenariusz główny:**  
**1.** Aktor naciska odpowiedni przycisk  
**2.** System wyświetla aktorowi interfejs płatności

**Nazwa przypadku:** Wyświetlenie aktualnej sumy zapłaconej kwoty  
**Aktor:** Użytkownik  
**Wyzwalacz:** Aktor znajduje się w interfejsie płatności  
**Scenariusz główny:**  
**1.** System wyświetla informacje o wysokości aktualnie zapłaconej kwoty

**Nazwa przypadku:** Zakończenie transakcji po minucie bezczynności  
**Aktor:** Użytkownik  
**Wyzwalacz:** Aktor po naciśnieciu przycisku wyboru rodzaju biletu, nie wykonał żadnych działań przez minutę  
**Scenariusz główny:**  
**1.** System oblicza czas od ostatniej wykonanej aktywności  
**2.** System zmienia interfejs płatności na główny interfejs aplikacji

**Nazwa przypadku:** Wyświetlenie informacji o niepowodzeniu transakcji  
**Aktor:** Użytkownik  
**Wyzwalacz:** System zakończył transakcje przez brak aktywności  
**Scenariusz główny:**  
**1.** System wyświetla aktorowi informacje o niepowodzeniu transakcji

**Nazwa przypadku:** Włożenie monet/banknotów  
**Aktor:** Użytkownik  
**Wyzwalacz:** Aktor znajduje się w interfejsie płatności  
**Scenariusz główny:**  
**1.** Aktor wybiera odpowiedni nominał  
**2.** Aktor przeciąga wybrany nominał na automat biletowy

**Nazwa przypadku:** Zatwierdzenie kwoty  
**Aktor:** Użytkownik  
**Wyzwalacz:** Aktor znajduje się w interfejsie płatności  
**Scenariusz główny:**  
**1.** Aktor naciska przycisk odpowiedzialny za zatwierdzenie kwoty

**Nazwa przypadku:** Sprawdzenie, czy suma zapłaconej kwoty przekracza cenę biletu  
**Aktor:** Użytkownik  
**Wyzwalacz:** Aktor nacisnął przycisk odpowiednialny za zatwierdzenie kwoty  
**Scenariusz główny:**  
**1.** System porównuje wprowadzoną kwotę z ceną przypisaną do wybranego biletu

**Nazwa przypadku:** Wyświetlenie informacji o braku wystarczającej kwoty  
**Aktor:** Użytkownik  
**Wyzwalacz:** Kwota wprowadzonaa przez użytkownika jest niższa niż cena wybranego biletu  
**Scenariusz główny:**  
**1.** System wyświetla aktorowi informację o niewystarczającej kwocie

**Nazwa przypadku:** Obliczenie reszty do wydania  
**Aktor:** Użytkownik  
**Wyzwalacz:** Kwota wprowadzonaa przez użytkownika jest wyższa niż cena wybranego biletu  
**Scenariusz główny:**  
**1.** System oblicza kwotę, którą musi wydać użytkownikowi

**Nazwa przypadku:** Wydanie reszty  
**Aktor:** Użytkownik  
**Wyzwalacz:** System obliczył kwotę, która ma do wydania aktorowi  
**Scenariusz główny:**  
**1.** System wydaje aktorowi odpowiednią kwotę

**Nazwa przypadku:** Wydanie biletu  
**Aktor:** Użytkownik  
**Wyzwalacz:** Użytkownik wprowadził odpowiednią kwotę i ją zatwierdził  
**Scenariusz główny:**  
**1.** System wydaje aktorowi bilet

**Nazwa przypadku:** Wyświetlenie informacji o powodzeniu transakcji  
**Aktor:** Użytkownik  
**Wyzwalacz:** Cała tranzakcja przebiegła pomyślnie (aktor otrzymał bilet oraz resztę)  
**Scenariusz główny:**  
**1.** System wyświetla aaktorowi komunikat o poprawnym przebiegu transakcji

### **4. Wymagania funkcjonalne i niefunkcjonalne.**

**Wymagania funkcjonalne:**

· Możliwość kupna dwóch rodzajów biletów: normalnego i ulgowego

· Możliwość płatności wieloma rodzajami monet i banknotów

· Zwracanie reszty

· Wyświetlanie informacji o brakującej kwocie

· Wyświetlanie informacji o powodzeniu transakcji

· Wyświetlanie informacji o niepowodzeniu transakcji

· Zakończenie transakcji po minucie bezczynności

**Wymagania niefunkcjonalne:**

· Przejrzysty i intuicyjny interfejs

· Łatwa możliwość wyboru rodzaju biletów

· Szybka weryfikacja rodzaju monet i banknotów

### **5. Wybranie systemu kontroli wersji oraz platformy hostingu dla niej**

Jako system kontroli wersji został wybrany Git oraz GitHub jako platforma hostingowa.

### **6. Wskazanie metodologii programowania zwinnego i raport z metodologii programowania zwinnego**

Jako metodologia programowania zostało wybrane Jira software.
W panelu Jira zostały utworzone zadania dla każdego z członków zespołu:
1.    Wstępny opis działania programu - Damian Zawisza 
2.    Analiza MoSCoW - Jakub Nykiel
3.    Diagram przypadków użycia - Mirosław Jachowicz
4.    Wymagania funkcjonalne i niefunkcjonalne - Rafał Majchrowicz
5.    Wybranie systemu kontroli wersji oraz platformy hostingu dla niej, utworzenie repozytorium - Rafał Majchrowicz
6.    Raport ze stosowania metodologii programowania zwinnego - Jakub Nykiel

Poniżej znajduje się załącznik z screenshotem z powyższych zadań z panelu Jira:
https://ibb.co/3dXh7kp

## Strona startowa, należy wybudzić urządzenie a by prześć do zakładki z biletami.Po dłuższej nieaktywności biletomat powraca właśnie do niej. ##

class Start_page:

    def configure_master(self):
        self.master.geometry("1500x900")
        self.master.config(bg="white")
        self.master.title("Automat biletowy")

    def __init__(self, builder):
        self.width = builder.width
        self.height = builder.height
        self.white = builder.white
        self.master = builder.master

        self.configure_master()
        self.frame = builder.frame
        self.image_button = builder.image_button



## Zakładka z biletami. Możliwość wyboru biletu ulgowego i normalnego. ##

class Bilet_page:

    def configure_master(self):
        self.master.geometry("1500x900")
        self.master.config(bg="white")
        self.master.title("Automat biletowy")

    def __init__(self, builder):
        self.width = builder.width
        self.height = builder.height
        self.white = builder.white
        self.master = builder.master

        self.configure_master()
        self.frame = builder.frame
        self.image_button = builder.image_button

    class BiletBuilder:

        def __init__(self):
            self.master = Tk()
            self.width = 50
            self.height = 10
            self.frame = tk.Frame(self.master, width=500)
            self.white = "white"
            self.image_button = PhotoImage(file=r"C:\Users\Krecik\Desktop\pythonProject\button.png")

        def change_page(self, page):
            factory_page(page)

        def buttons(self, frame):
            width_image = 30
            height_image = 10

            image = self.image_button.zoom(19, 19).subsample(39)

            b0 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b1 = tk.Button(b1_label, image=image, background=self.white, command= lambda : self.change_page(2))
            b1.image = image

            b1.grid()

            b2 = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3_label = tk.Label(frame, width=width_image, height=height_image, background=self.white)
            b3 = tk.Button(b3_label, image=image)

            b3.grid()

            b4 = tk.Label(frame, width=width_image, height=height_image, background=self.white)

            b0.grid(row=0, column=0)
            b1_label.grid(row=1, column=0)
            b2.grid(row=2, column=0)
            b3_label.grid(row=3, column=0)
            b4.grid(row=4, column=0)

        def left(self):
            l0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l1 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue",
                          text="Bilet Ulgowy")
            l2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l3 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue")
            l4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            l0.grid(row=0, column=0)
            l1.grid(row=1, column=0)
            l2.grid(row=2, column=0)
            l3.grid(row=3, column=0)
            l4.grid(row=4, column=0)

        def center(self):
            m0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m1 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m3 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            m0.grid(row=0, column=1)
            m1.grid(row=1, column=1)
            m2.grid(row=2, column=1)
            m3.grid(row=3, column=1)
            m4.grid(row=4, column=1)

        def right(self):
            r0 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            r1 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue",
                          text="Bilet Normalny")
            r2 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)
            r3 = tk.Label(frame_center, width=self.width, height=self.height, background="lightblue")
            r4 = tk.Label(frame_center, width=self.width, height=self.height, background=self.white)

            r0.grid(row=0, column=2)
            r1.grid(row=1, column=2)
            r2.grid(row=2, column=2)
            r3.grid(row=3, column=2)
            r4.grid(row=4, column=2)

        def create_center(self):
            global frame_center
            frame_center = tk.Frame(self.frame, highlightbackground="black", highlightthickness="5")
            self.left()
            self.center()
            self.right()
            frame_center.grid(row=1, column=1)

        def create_top(self):
            frame_top = tk.Frame(self.frame, height=50, background=self.white)
            frame_top.grid(row=0, column=0)

        def create_right(self):
            frame_right = tk.Frame(self.frame, width=100)
            self.buttons(frame_right)
            frame_right.grid(row=1, column=2)

        def create_left(self):
            frame_left = tk.Frame(self.frame, width=100)
            self.buttons(frame_left)
            frame_left.grid(row=1, column=0)


        def create(self):
            self.create_left()
            self.create_top()
            self.create_center()
            self.create_right()
            self.frame.pack()


        def build(self):
            self.create()
            mainloop()

## Link do projektu na Figmie: ##
https://www.canva.com/design/DAGAum7-1Fs/h66BKcrA4z2E_b1GyXD5rA/edit?utm_content=DAGAum7-1Fs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Raport ze stosowania metodologii programowania zwinnego: ##
![JiraII](JiraII.png)


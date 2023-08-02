from docxtpl import DocxTemplate
from dataclasses import dataclass, field
import os
import sys
import datetime
from abc import ABC, abstractmethod

LIST_PUSAT = []
LIST_DAERAH = []
LIST_DESA = []
LIST_KELOMPOK = []
LIST_KHUSUS = []

class InterfaceMembers(ABC):
    @abstractmethod
    def show_member_detail():
        pass

class Person(InterfaceMembers):
    def __init__(self, name):
        self.name = name

    def show_member_detail(self):
        return self.name
    
class Member(InterfaceMembers):
    def __init__(self):
        self.list_member = []

    def show_member_detail(self):
        for member in self.list_member:
            member.show_member_detail()

    def add(self, member):
        self.list_member.append(member)

    def remove(self, member):
        self.list_member.remove(member)



@dataclass
class Setoran:
    datetime: str = field(init=False)
    jenis: str
    nama: str
    bulan: str = field(default_factory=str, init=False)
    amount: int

    def __post_init__(self):
        self.datetime = datetime.datetime.now()
        if self.bulan == "":
            self.bulan = self.datetime.strftime("%m")

@dataclass
class Jamaah:
    name: str
    setoran : list[Setoran] = field(default_factory=list, init=False)

    def add_setoran(self, jenis, nama, amount):
        setoran = Setoran(jenis, nama, amount)
        self.setoran.append(setoran)

    @property
    def total(self):
        total= [x.amount for x in self.setoran]
        return sum(total)


# j1 = Jamaah(name="Erfan")
# j1.add_setoran("setoran daerah", "Kas Daerah", 50000)
# print(j1.total)
# j1.add_setoran("setoran desa", "Kas Desa", 1000000)
# j1.add_setoran("setoran kelompok", "Kas Kelompok", 2000000)
# j1.add_setoran("setoran kelompok", "Kas Kelompok", 300000)
# print(j1, j1.total)


def selection_type(ops):
    print("""Please choose following to enter the values:
              1. Setoran Pusat
              2. Setoran Daerah
              3. Setoran Desa
              4. Setoran Kelompok
              5. Setoran Khusus
              
              """)
    print("="*20)

    match ops:
        case "1": 
            command = input("Choose the command : ")
            text = input("Input text : ")
            amount = input("Input amount : ")

            create_data(command, text, amount)
        case "2": 
            command = input("Choose the type :")
            view_data(command)


def view_data(type):
     match type:
          case "1": 
             subtotal = total(LIST_PUSAT)
             print(subtotal)

def create_data(type: str, text: str, amount: int) -> None:
     data = [text, amount]
     match type:
          case "1": 
             LIST_PUSAT.append(data)
             print("Sukses input Setoran Daerah")
          case "2": 
             LIST_DAERAH.append(data)
             print("Sukses input Setoran Daerah")
          case "3": 
             LIST_DESA.append(data)
             print("Sukses input Setoran Desa")
          case "4": 
             LIST_KELOMPOK.append(data)
             print("Sukses input Setoran Kelompok")
          case "5": 
             LIST_KHUSUS.append(data)
             print("Sukses input Setoran Khusus")

     

def total(list: list[int]) -> int:
    list_int = [int(x[1]) for x in list]

    return sum(list_int)

def save_doc():
    doc.render({"month": "July", "year": "2023", "setoran_daera": list_setoran_daerah, "total_daerah": total(list_setoran_daerah), "names": list_agnia_daerah, "total_agnia": total(list_agnia_daerah)})

    doc.save("generated-from-python.docx")


def cli_app():
    
    match os.name:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

    while True:
        print("="*20)

        print("Welcome to the Kas Kelompok Ngaliyan 2")

        print("="*20)

        print("""Please choose following to enter the values:
              1. Create Data
              2. View Data
              3. Edit Data
              4. Delete Data
              
              """)
            
        command = input("Choose the command : ")
        match command:
            case "1": selection_type("1")
            case "2": selection_type("2")
            case "3": selection_type("2")
            case "4": selection_type("2")

        
        end = input("Are you sure want to continue : ")
        if end.lower() == "y" or end.lower() == "yes":
             continue
        else: sys.exit()


# if __name__ == "__main__":
#     cli_app()


doc = DocxTemplate("Laporan Setoran Bulanan - python.docx")

list_setoran_daerah = [["Infaq Rizky (IR)", 6413000], ["Sodaqoh Rutin (SR)", 2590000], ["Syiar-syiar", 228000]]
list_setoran_desa = [["Sodaqoh Rutin", 50000]]
list_agnia_daerah = [["Bpk. Sutimin", 50000], ["Bpk. Erfan Huda", 9000000]]

doc.render({"month": "July", "year": "2023", "setoran_daera": list_setoran_daerah, "total_daerah": total(list_setoran_daerah), "names": list_agnia_daerah, "total_agnia": total(list_agnia_daerah)})
doc.save("generated-from-python.docx")
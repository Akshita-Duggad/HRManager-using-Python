from tmcomponents.components import Menu
from common.hr import Designation,ValidationException
from network_common.wrappers import Request,Response
from network_client.client import NetworkClient
import json

class HRClientUI:
    def __init__(self):
        pass
    def add_designation(self):
        title=input("Enter designation to add : ")
        designation=Designation(0,title)
        request=Request(manager="DesignationManager",action="add",request_object=designation)
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            print("Designation added")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])    

    def edit_designation(self):
        code=int(input("Enter code to update : "))
        title=input("Enter designation to update : ")
        designation=Designation(code,title)
        request=Request(manager="DesignationManager",action="edit",request_object=designation)
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            print("Designation updated")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])    

    def delete_designation(self):
        code=int(input("Enter code to delete : "))
        designation=Designation(code,"aa")
        request=Request(manager="DesignationManager",action="delete",request_object=designation)
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            print("Designation deleted")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])    

    def get_designation(self):
        code=int(input("Enter code to search : "))
        designation=Designation(code,"aa")
        request=Request(manager="DesignationManager",action="search",request_object=designation)
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            designation=Designation.from_json(response.result_json_string)
            print(f"Code : {designation.code}, Title : {designation.title}")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])    

    def get_all_designations(self):
        request=Request(manager="DesignationManager",action="getAll")
        network_client=NetworkClient()
        response=network_client.send(request)
        if response.success:
            designations=json.loads(response.result_json_string)
            designationsList=list(map(lambda obj: Designation(**obj),designations))
            for designation in designationsList:
                print(f"Code : {designation.code}, Title : {designation.title}")
        else:
            validationException=ValidationException.from_json(response.error_json_string)
            if validationException.message and len(validationException.message)>0: print(validationException.message)
            if validationException.exceptions:
                for exception in validationException.exceptions.values():
                    print(exception[1])    


def main_menu_handler(menu,choice):
    if choice==1: designation_menu.activate()
    if choice==2: employee_menu.activate()
    if choice==3: menu.deactivate()

def designation_menu_handler(menu,choice):
    if choice==1: 
        hr_client_ui=HRClientUI()
        hr_client_ui.add_designation()
    if choice==2: 
        hr_client_ui=HRClientUI()
        hr_client_ui.edit_designation()
    if choice==3: 
        hr_client_ui=HRClientUI()
        hr_client_ui.delete_designation()
    if choice==4: 
        hr_client_ui=HRClientUI()
        hr_client_ui.get_designation()
    if choice==5: 
        hr_client_ui=HRClientUI()
        hr_client_ui.get_all_designations()


    if choice==6: menu.deactivate()

def employee_menu_handler(menu,choice):
    if choice==6: menu.deactivate()

main_menu=Menu("Main Menu",main_menu_handler)
main_menu.add_option("Designation Master")
main_menu.add_option("Employee Master")
main_menu.add_option("Exit")

designation_menu=Menu("Designation Master",designation_menu_handler)
designation_menu.add_option("Add")
designation_menu.add_option("Edit")
designation_menu.add_option("Delete")
designation_menu.add_option("Search")
designation_menu.add_option("Display list")
designation_menu.add_option("Exit")

employee_menu=Menu("Employee Master",employee_menu_handler)
employee_menu.add_option("Add")
employee_menu.add_option("Edit")
employee_menu.add_option("Delete")
employee_menu.add_option("Search")
employee_menu.add_option("Display list")
employee_menu.add_option("Exit")

main_menu.activate()

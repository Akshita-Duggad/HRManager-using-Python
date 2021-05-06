from network_server.server import NetworkServer
from network_common.wrappers import Request,Response
import common.hr
import data_layer.hr
import json
from data_layer.hr import HRDLHandler,DataLayerException
from common.hr import ValidationException
def requestHandler(request):
    if request.manager=="DesignationManager":
        if request.action=="add":
            designation=common.hr.Designation.from_json(request.json_string)
            if designation.has_exceptions:
                validationException=ValidationException(exceptions=designation.exceptions)
                response=Response(success=False,error=validationException)
                return response

            dlDesignation=data_layer.hr.Designation(designation.code,designation.title)
            if dlDesignation.has_exceptions:
                validationException=ValidationException(exceptions=dlDesignation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            try:
                HRDLHandler.add_designation(dlDesignation) 
                response=Response(success=True)
                return response

            except DataLayerException as err:
                validationException=ValidationException(err.message,err.exceptions)
                response=Response(success=False,error=validationException)
                return response


        if request.action=="edit":
            designation=common.hr.Designation.from_json(request.json_string)
            if designation.has_exceptions:
                validationException=ValidationException(exceptions=designation.exceptions)
                response=Response(success=False,error=validationException)
                return response

            dlDesignation=data_layer.hr.Designation(designation.code,designation.title)
            if dlDesignation.has_exceptions:
                validationException=ValidationException(exceptions=dlDesignation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            try:
                HRDLHandler.update_designation(dlDesignation) 
                response=Response(success=True)
                return response

            except DataLayerException as err:
                validationException=ValidationException(err.message,err.exceptions)
                response=Response(success=False,error=validationException)
                return response


        if request.action=="delete":
            designation=common.hr.Designation.from_json(request.json_string)
            if designation.has_exceptions:
                validationException=ValidationException(exceptions=designation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            try:
                HRDLHandler.delete_designation(designation.code) 
                response=Response(success=True)
                return response

            except DataLayerException as err:
                validationException=ValidationException(err.message,err.exceptions)
                response=Response(success=False,error=validationException)
                return response


        if request.action=="search":
            designation=common.hr.Designation.from_json(request.json_string)
            if designation.has_exceptions:
                validationException=ValidationException(exceptions=designation.exceptions)
                response=Response(success=False,error=validationException)
                return response
            try:
                dlDesignation=HRDLHandler.get_designation_by_code(designation.code) 
                designation=common.hr.Designation(dlDesignation.code,dlDesignation.title)
                response=Response(success=True,result_object=designation)
                return response

            except DataLayerException as err:
                validationException=ValidationException(err.message,err.exceptions)
                response=Response(success=False,error=validationException)
                return response

        if request.action=="getAll":
            try:
                designations=HRDLHandler.get_designations() 
                response=Response(success=True)
                response.result_json_string=json.dumps(designations,indent=4,default=lambda obj: obj.__dict__)
                return response

            except DataLayerException as err:
                validationException=ValidationException(err.message,err.exceptions)
                response=Response(success=False,error=validationException)
                return response



network_server=NetworkServer(requestHandler)
network_server.start()
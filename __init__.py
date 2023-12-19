# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os.path
import sys
import io

base_path = tmp_global_obj["basepath"] #type: ignore
cur_path = base_path + 'modules' + os.sep + 'GoogleSlides' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
    sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
    sys.path.append(cur_path_x86)

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

import traceback
import pickle

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module") #type: ignore

global creds
global mod_sls_session

try:
    if not mod_sls_session : #type:ignore
        mod_sls_session = {}
except NameError:
    mod_sls_session = {}

session = GetParams("session") #type: ignore

if not session:
    session = ''

try:
    if module == "GoogleSuite":
        creds = None
        credential_path = GetParams("credentials_path") #type: ignore
        result = GetParams("result") #type: ignore

        if session == '':
            filename = "token_slides.pickle"
        else:
            filename = "token_slides_{s}.pickle".format(s=session)

        filename = os.path.join(base_path, filename)


        if not os.path.exists(credential_path):
            raise Exception("El archivo de credenciales no existe en la ruta especificada")
        
        try:
            SCOPES = [
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/presentations'
            ]

            if os.path.exists(filename):
                with open(filename, 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(credential_path, SCOPES)
                    creds = flow.run_local_server()
                with open (filename, 'wb') as token:
                    pickle.dump(creds, token)


            mod_sls_session[session] = creds

            SetVar(result, True)    #type: ignore

        except Exception as e:
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e
        
    if module == "createPresentation":

        title = GetParams("title")  #type: ignore
        result = GetParams("result_var")    #type: ignore

        try:            
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            presentation_body = {
                "title": title
            }

            request = service_slides.presentations().create(body=presentation_body)
            response = request.execute()
            
            SetVar(result, response["presentationId"])  #type: ignore

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            raise e

    if module == "addBlankSlide":
        slides_id = GetParams("id")
        result = GetParams("result")

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            request = {
                'createSlide': {
                    'slideLayoutReference': {
                        'predefinedLayout': 'BLANK'
                    }
                }
            }

            response = service_slides.presentations().batchUpdate(
                presentationId=slides_id, body={'requests': [request]}).execute()

            if result:
                new_slide_id = response.get("replies")[0].get("createSlide")['objectId']
                SetVar(result, new_slide_id)        
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e

    if module == "addLayoutSlide":
        slides_id = GetParams("id")
        result = GetParams("result_var")

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            request = {
                "createSlide": {
                    "slideLayoutReference": {
                        "predefinedLayout": 'TITLE_AND_BODY'
                    }
                }
            }
            
            response = service_slides.presentations().batchUpdate(
                presentationId=slides_id, body={'requests': [request]}).execute()


            newSlide_id = response.get("replies")[0].get("createSlide")
            SetVar(result, newSlide_id['objectId'])  
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e
        
    if module == "addText":

        page_id = GetParams("page")   #type: ignore
        presentation_id = GetParams("presentation") #type: ignore
        identificador = GetParams("element_id") #type: ignore
        result = GetParams("result_var")  #type: ignore
        text = GetParams("text")    #type: ignore
        tamano = GetParams("size")
        negrita = GetParams("bold")
        cursiva = GetParams("italic")
        subrayado = GetParams("underline")
        align = GetParams("alignment_text")
        color = GetParams("color")
        
        TextColors = {
            "black": {'red': 0.0, 'green': 0.0, 'blue': 0.0},
            "blue": {'red': 0.0, 'green': 0.0, 'blue': 1.0},
            "ligthBlue": {'red': 0.5, 'green': 0.7, 'blue': 1.0},
            "darkRed": {'red': 0.5, 'green': 0.0, 'blue': 0.0},
            "darkYellow": {'red': 0.5, 'green': 0.5, 'blue': 0.0},
            "gray25": {'red': 0.25, 'green': 0.25, 'blue': 0.25},
            "gray50": {'red': 0.5, 'green': 0.5, 'blue': 0.5},
            "green": {'red': 0.0, 'green': 1.0, 'blue': 0.0},
            "pink": {'red': 1.0, 'green': 0.7, 'blue': 0.7},
            "red": {'red': 1.0, 'green': 0.0, 'blue': 0.0},
            "teal": {'red': 0.0, 'green': 0.5, 'blue': 0.5},
            "white": {'red': 1.0, 'green': 1.0, 'blue': 1.0},
            "yellow": {'red': 1.0, 'green': 1.0, 'blue': 0.0}
        }

        if not tamano:
            tamano = 14

        if not color:
            color = "black"

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            paragraph_style = {
                
                'alignment' : align
            }
            text_style = {
                'foregroundColor': {'opaqueColor': {'rgbColor': TextColors[color]}},
                'fontSize': {'magnitude': tamano, 'unit': 'PT'},
                'bold': negrita,  
                'italic': cursiva,  
                'underline': subrayado  
            }
            height = {"magnitude": 300, "unit": "PT"}
            width = {"magnitude": 550, "unit": "PT"}
            requests = [
                {
                        "createShape": {
                            "objectId": identificador,
                            "shapeType": "TEXT_BOX",
                            "elementProperties": {
                                "pageObjectId": page_id,
                                "size": {"height": height, "width": width},
                                "transform": {
                                    "scaleX": 1,
                                    "scaleY": 1,
                                    "translateX": 100,
                                    "translateY": 100,
                                    "unit": "PT",
                                },
                            },
                        }
                    },
                {
                    'insertText': {
                        'objectId': identificador,
                        'insertionIndex': 0,
                        'text': text,
                    }
                },
                {
                    'updateTextStyle': {
                        'objectId': identificador,
                        'style': text_style,
                        "textRange": {"type": "ALL"},
                        'fields': 'foregroundColor,fontSize,bold,italic,underline'
                    }
                },
                {
                    'updateParagraphStyle': {
                        'objectId': identificador,
                        'style': paragraph_style,
                        "textRange": {"type": "ALL"},
                        'fields': 'alignment'
                    }
                }
            ]
        
            body = {"requests": requests}
            response = (
                service_slides.presentations()
                .batchUpdate(presentationId=presentation_id, body=body)
                .execute()
            )

            SetVar(result, identificador)

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "insertText":

        page_id = GetParams("page")   #type: ignore
        presentation_id = GetParams("presentation") #type: ignore
        identificador = GetParams("element_id") #type: ignore
        result = GetParams("result_var")  #type: ignore
        text = GetParams("text")    #type: ignore
        tamano = GetParams("size")
        negrita = GetParams("bold")
        cursiva = GetParams("italic")
        subrayado = GetParams("underline")
        align = GetParams("alignment_text")
        color = GetParams("color")
        
        TextColors = {
            "black": {'red': 0.0, 'green': 0.0, 'blue': 0.0},
            "blue": {'red': 0.0, 'green': 0.0, 'blue': 1.0},
            "ligthBlue": {'red': 0.5, 'green': 0.7, 'blue': 1.0},
            "darkRed": {'red': 0.5, 'green': 0.0, 'blue': 0.0},
            "darkYellow": {'red': 0.5, 'green': 0.5, 'blue': 0.0},
            "gray25": {'red': 0.25, 'green': 0.25, 'blue': 0.25},
            "gray50": {'red': 0.5, 'green': 0.5, 'blue': 0.5},
            "green": {'red': 0.0, 'green': 1.0, 'blue': 0.0},
            "pink": {'red': 1.0, 'green': 0.7, 'blue': 0.7},
            "red": {'red': 1.0, 'green': 0.0, 'blue': 0.0},
            "teal": {'red': 0.0, 'green': 0.5, 'blue': 0.5},
            "white": {'red': 1.0, 'green': 1.0, 'blue': 1.0},
            "yellow": {'red': 1.0, 'green': 1.0, 'blue': 0.0}
        }

        if not tamano:
            tamano = 14

        if not color:
            color = "black"

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            paragraph_style = {
                
                'alignment' : align
            }

            text_style = {
                'foregroundColor': {'opaqueColor': {'rgbColor': TextColors[color]}},
                'fontSize': {'magnitude': tamano, 'unit': 'PT'},
                'bold': negrita,  
                'italic': cursiva,  
                'underline': subrayado  
            }

            requests = [
                {
                    'insertText': {
                        'objectId': identificador,
                        'insertionIndex': 0,
                        'text': text,
                    }
                },
                {
                    'updateTextStyle': {
                        'objectId': identificador,
                        'style': text_style,
                        "textRange": {"type": "ALL"},
                        'fields': 'foregroundColor,fontSize,bold,italic,underline'
                    }
                },
                {
                    'updateParagraphStyle': {
                        'objectId': identificador,
                        'style': paragraph_style,
                        "textRange": {"type": "ALL"},
                        'fields': 'alignment'
                    }
                }
            ]
        
            body = {"requests": requests}
            response = (
                service_slides.presentations()
                .batchUpdate(presentationId=presentation_id, body=body)
                .execute()
            )

            SetVar(result, identificador)
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "deleteText":
        presentation_id = GetParams("p_id") #type: ignore
        page_id = GetParams("s_id")     #type: ignore
        identificador = GetParams("object_id")      #type: ignore
        result = GetParams("result_var")  #type: ignore

        try:

            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            request = {
                "deleteText": {
                    "objectId": identificador,
                    "textRange": {"type": "ALL"},
                }
            }

            body = {"requests": request}
            response = (
                service_slides.presentations()
                .batchUpdate(presentationId=presentation_id, body=body)
                .execute()
            )
            
            if result:
                SetVar(result, True) #type: ignore

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e


    if module == "deletePresentation":
        presentation_id = GetParams("p_id") #type: ignore
        result = GetParams("result_var")  #type: ignore

        try:
            service_drive = build('drive', 'v3', credentials=mod_sls_session[session])

            file_metadata = service_drive.files().get(fileId=presentation_id).execute()

            service_drive.files().delete(fileId=presentation_id).execute()
            
            
            if result:
                SetVar(result, True) #type: ignore

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e

    if module == "deleteSlide":
        slide_id = GetParams("slide")   #type: ignore
        presentation_id = GetParams("id")
        result = GetParams("result_var")  #type: ignore

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])

            request = {
                'deleteObject': {
                    'objectId': slide_id
                }
            }

            body = {'requests': [request]}
            response = service_slides.presentations().batchUpdate(
                    presentationId=presentation_id,
                    body=body).execute()
            
            if result:
                SetVar(result, True)

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()
            SetVar(result, False)
            raise e


    if module == "getInfo":

        presentation_id = GetParams("p_id")
        nro_page = GetParams("slide")
        result = GetParams("result_var")

        try:
            service_slides = build('slides', 'v1', credentials=mod_sls_session[session])
            res = []
            nro_page = eval(nro_page)
            response = service_slides.presentations().get(presentationId=presentation_id).execute()
            slides = response.get('slides', [])

            if slides:
                page = slides[nro_page]

            for page_element in page.get('pageElements', []):
                object_id = page_element.get('objectId')
              
                res.append(object_id)                

            SetVar(result, res)

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "downloadSlides":

        presentation_id = GetParams("p_id") #type: ignore
        export_format = GetParams("format")   #type: ignore
        result = GetParams("result_var")  #type: ignore
        file_path = GetParams("path_file")     #type: ignore
        
        try:

            if not presentation_id:
                raise Exception("ID de Slides no enviado")

            if not file_path:
                raise Exception("No se ingreso ruta donde guardar el archivo")
            
            export_formats = {
                "PDF (.pdf)": "application/pdf",
                "Microsoft PowerPoint (.pptx)": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            }

            mime = export_formats.get(export_format)

            service_drive = build('drive', 'v3', credentials=mod_sls_session[session])

            file = service_drive.files().get(fileId=presentation_id, supportsAllDrives=True).execute()
            request = None

            request = service_drive.files().export_media(fileId=presentation_id, mimeType=mime)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)

            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))

            extension = export_format.split()[-1][1:-1]
            
            with io.open(file_path + os.sep + file['name'] + extension, 'wb') as out:
                fh.seek(0)
                out.write(fh.read())

            if result:
                SetVar(result, True)

        except Exception as e:
            import traceback
            traceback.print_exc()
            PrintException()    #type: ignore
            SetVar(result, False)   #type: ignore
            raise e

except Exception as e:
    import traceback
    traceback.print_exc()
    PrintException()
    raise e
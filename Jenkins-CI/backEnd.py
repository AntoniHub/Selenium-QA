import sys
import pprint
import unittest
import requests
import firebase_admin
from faker import Faker
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\AntonioRodriguezFarias\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

fake = Faker('es_ES')
s = requests.session()

with open("API_KEY.txt", "r", encoding="utf-8") as key:
    for api in key:
        api = api.strip()
        API_KEY = api

#
#
##################
###  Campaigns ###
##################
#
# GET -> /campaigns/client/{client_id}
# GET -> /campaigns/client/{clientID}/campaign/{campaignID}
# POST -> /campaigns
# POST -> /campaigns/client/{client_id}
# DELETE -> /campaigns/client/{clientID}/campaign/{campaignID}
#
# Obtenemos Campañas de Phishing del cliente -> Z488h4SK0hr1Wx5Sat6l
#


class TestPhishingAPI(unittest.TestCase):
    def test_01_obtainCampaign(self):
        print('\n**********  Campaigns  **********')
        print('Starting -> Campaigns')
        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            # auth=TokenAuth(f'{APY_KEY}'),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        # self.assertEqual(r.status_code, 200)
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Obtener campaña especifica de cliente -> 3hqrdtgh23pXcnYoZjaB9
    # GET -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Retrieve a campaign associated to a client
    #

    def test_02_retrieveCampaign(self):
        print('\nGetting campaign associated to a client')
        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Comprobar recepcion (campaña de prueba) en el cliente -> Z488htew23r1Wx5Sat6l
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Create a test campaign
    #

    def test_03_checkCampaign(self):
        print('\nCreating a TEST Campaign')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "custom_name": "Coronavirus (Covid 19)",
                "campaign_type": "coronavirus_campaign-es",
                "destinations": [{
                    "email": "abgrodriguezfarias@gmail.com",
                    "first_name": "Antonio",
                    "last_name": "Rodriguez",
                    "position": ""
                }],
                "customization": {
                    "company": "TEST Prueba",
                    "email": "abgordriguezfarias@gmail.com"
                }
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Creamos Campaña en el cliente -> Z488h4kst34r1Wx5Sat6l
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Create Campaign
    #

    def test_04_createCampaign(self):
        print('\nCreating Campaign')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "custom_name": "Coronavirus (Covid 19)",
                "campaign_type": "coronavirus_campaign-es",
                "destinations": [{
                    "email": "abgrodriguezfarias@gmail.com",
                    "first_name": "Antonio",
                    "last_name": "Rodriguez",
                    "position": ""
                }],
                "customization": {
                    "company": "TEST Prueba",
                    "email": "abgrodriguezfarias@gmail.com"
                }
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # DELETE -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Una vez eliminada la campaña del cliente en Cyber Guardian
    # Conectamos con Firebase para tambien eliminar el documento correspondiente en el cliente -> Z488h4SK0hr1Wx5Sat6l
    # Delete Campaign previously created
    #

    def test_05_deleteCampaign(self):
        print('\nDeleting Campaign')
        verify = db.collection(u'clients').document(u'Z48123asdK0hr1Wx5Sat6l').collection('campaigns').get()
        pp = pprint.PrettyPrinter(indent=4)
        for x in verify:
            if x.exists:
                y = x.get('campaign_id')

                #
                # Tenemos el ID de la campaña creada
                # Ahora la seteamos en la URL para realizar el DELETE
                # Este DELETE elimina la campaña SOLO de Cyber Guardian (aun estara el documento en campaigns)
                #

                r = s.delete(
                    'https://api-testing.ardoriguezf.es/{}'.format(y),
                    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
                )
                if r.status_code == 204:
                    print("-------------------------------------------------")
                    print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
                    print("-------------------------------------------------")
                else:
                    print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
                    sys.exit()

                #
                # Consultamos y eliminamos la campaña de Firestore
                #

                verify2 = db.collection(u'clients').document(u'Z488fgh223hr1Wx5Sat6l').collection('campaigns').document(
                    '{}'.format(y)).get()
                if verify2.exists:
                    """pp.pprint(verify2.to_dict())"""
                    db.collection(u'clients').document(u'Z488h4ghw241Wx5Sat6l').collection('campaigns').document(
                        '{}'.format(y)).delete()

#
#
#
#
#######################
######  CLIENTS  ######
#######################
#
# PUT -> /clients/{clientId}/tags/{tagId}
# PUT -> /clients/{clientId}/tags/members
# PUT -> /clients/billing-address
# POST -> /clients/{clientId}/members
# POST -> /clients/contact-request
# POST -> /clients/{clientId}/members/bulk
# POST -> /clients/{clientId}/tags
# DELETE -> /admin/clients/{client}/members/{member}
# DELETE -> /clients/{clientId}/tags/{tagId}
#
# Creamos team_member en el cliente -> Z488h4SK0hr1Wx5Sat6l
# POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
# Create team_member
#


class TestClients(unittest.TestCase):
    def test_06_createTeamMember(self):
        print('\n\n**********  Clients  **********')
        print('Starting -> Clients \n    Create team_member')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "name": "Alejandro",
                "surname": "Farias",
                "email": "arodriguez@gmail.com",
                "language": "es",
                "role": "employee"
            }
        )
        if r.status_code == 201:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Eliminamos el team_member anteriormente creado
    # DELETE -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Delete team_member previously created
    #

    def test_07_delete_team_member(self):
        # Conectamos con Firebase para obtener el ID del team_member creado
        # Obteniendo ID de team_member creado
        #

        verify = db.collection(u'clients').document(u'Z488h4Stre76x5Sat6l').collection(u'members').where(
            u'email', u'==', u'arodriguez@gmail.com').get()
        pp = pprint.PrettyPrinter(indent=4)
        for x in verify:
            if x.exists:
                member_id = x.id
                # db.collection(u'clients').document(u'Z488h4SKasd45Wx5Sat6l').collection(u'members').document('{}'.format(id)).delete()
                """print('\n    Team Member -> {} was removed'.format(member_id))"""
                """print("----------------------------------------------------------------------------")"""

        print('\nDeleting Team Member')
        r = s.delete(
            'https://api-testing.ardoriguezf.es/{}'.format(member_id),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 204:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('ERROR  -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Crear team_members en masa -> Lista .CSV / .XLSX
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Create team_member in Bulk
    #

    def test_08_create_team_member_bulk(self):
        print('\nCreate member in BULK')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "membersToCreate": [{
                    "name": "Antonio",
                    "surname": "Rodriguez",
                    "email": "arodriguez@gmail.com",
                    "language": "es",
                    "role": "employee"

                }]  # Se crea solo 1 team_member por practicidad pero es un array
            }
        )
        if r.status_code == 201:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Eliminamos member in BULK
    # DELETE -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Delete team_member previously created
    #

    def test_09_delete_team_member_bulk(self):
        # Conectamos con Firebase para obtener ID de team_member creado
        # Obteniendo ID de member in BULK previamente creado
        #

        verify = db.collection(u'clients').document(u'Z48lk192K0hr1Wx5Sat6l').collection(u'members').where(
            u'email', u'==', u'arodriguez@gmail.com').get()
        pp = pprint.PrettyPrinter(indent=4)
        for x in verify:
            if x.exists:
                member_ID = x.id
                # db.collection(u'clients').document(u'Z4r3poSK0hr1Wx5Sat6l').collection(u'team_members').document('{}'.format(member_id)).delete()
                """print('\n    Team Member -> {} was removed'.format(member_id))"""
                """print("----------------------------------------------------------------------------")"""

        print('\nDeleting Team Member in BULK')
        r = s.delete(
            'https://api-testing.ardoriguezf.es/{}/'.format(member_ID),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 204:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('ERROR  -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Creamos etiqueta en un team_member
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Create TAG in teamMember: 40b5066a0e91ylsw296seb3883f6f60a9b98387506faf8
    #

    def test_10_create_tag(self):
        print('\nCreating TAG')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "tag": "TAG_test",
                "color": "#FFFFFF",
                "members": [
                    "40b5066a0e9111ftwvc9869ceb3883f6f60a9b98387506faf8"
                ]
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Cambiamos el color de la etiqueta
    # PUT -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Update color TAG
    #

    def test_11_update_tag(self):
        # Obtenemos ID de la etiqueta anteriormente creada
        #

        verify = db.collection(u'clients').document(u'Z488h4Sxmwu1Wx5Sat6l').collection(u'team_members').document(
            '40b5066a0e9111fbkjh23sp3f6f60a9b98387506faf8').get()
        if verify.exists:
            """print(verify2.to_dict())"""
            y = verify.get('tags')
            TAG = y[2]  # El cliente tiene dos etiquetas previas

        print('\nUpdating color TAG')
        r = s.put(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "tag": "{}".format(TAG),
                "color": "{}".format(fake.safe_hex_color()),  # Se utiliza libreria Faker para generar datos aleatorios
                "members": [
                    "40b5066a0e9111fb1dfH789ceb3883f6f60a9b98387506faf8"  # Admin OWNER
                ]
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('ERROR  -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Asignamos etiqueta a otro miembro
    # PUT -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Update TAG for given members
    #

    def test_12_tag_other_member(self):
        # Obtenemos ID de la etiqueta anteriormente creada
        #

        verify = db.collection(u'clients').document(u'Z488h4SvWbr1Wx5Sat6l').collection(u'members').document(
            '40b5066asdkw45fe6be3d29ceb3883f6f60a9b98387506faf8').get()
        if verify.exists:
            """print(verify2.to_dict())"""
            y = verify.get('tags')
            TAG = y[2]  # El cliente tiene dos etiquetas previas

        print('\nUpdating TAG for given members')
        r = s.put(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "members": [
                    "f94b74f6835ec187938976656f7265f7648ps3935792f3fb71"
                ],
                "to_tag": [
                    "{}".format(TAG)
                ]
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()
    #
    #
    #
    # Eliminamos etiqueta anteriormente creada
    # DELETE -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Delete TAG previously created
    #

    def test_13_delete_tag(self):
        # Obtenemos ID de la etiqueta anteriormente creada
        #

        verify = db.collection(u'clients').document(u'Z488h4PXkl3r1Wx5Sat6l').collection(u'members').document(
            '40b5066a0e9111fb121afeeb3883f6f60a9b9888sf2506faf8').get()
        if verify.exists:
            """print(verify2.to_dict())"""
            y = verify.get('tags')
            TAG = y[2]  # El cliente tiene dos etiquetas previas

        print('\nDeleting TAG')
        r = s.delete(
            'https://api-testing.ardoriguezf.es/{}'.format(TAG),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('ERROR  -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Actualizar datos de facturacion
    # PUT -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Update billing address of a client
    #

    def test_14_update_billing_address(self):
        # Obtenemos Bearer token para poder realizar siguientes requests
        # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
        # Obtain Bearer token - SignIn
        #

        print('\nGenerating bearer token')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            json={
                "email": "abgrodriguezfarias@gmail.com",
                "password": "T3st.1234"
            }
        )

        token = r.json()
        ACCESS_TOKEN = token.get('data')  # Bearer token en variable ACCESS_TOKEN

        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

        print('\nUpdate Billing address')
        r = s.put(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                     'Authorization': f'Bearer {ACCESS_TOKEN}'},
            json={
                "corporateName": "test",
                "line1": "Calle",
                "city": "Valencia",
                "state": "Valencia",
                "postalCode": "46006",
                "country": "Spain"
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Enviar numero de telefono a Atencion al cliente a traves del Te llamamos
    # Puede devolver 403 por reCaptcha -> El Te llamamos tiene reCaptcha y este a su vez, tiene un umbral elevado
    #

    def test_15_te_llamamos(self):
        # Obtenemos Bearer token para poder realizar siguientes requests
        # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
        # Obtain Bearer token - SignIn
        #

        print('\nGenerating bearer token')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            json={
                "email": "abgrodriguezfarias@gmail.com",
                "password": "T3st.1234"
            }
        )

        token = r.json()
        ACCESS_TOKEN = token.get('data')  # Bearer token en variable ACCESS_TOKEN

        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

        try:
            # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
            # requestContact
            print('\nSending contact-request')
            """with open("access_token.txt", "r", encoding="utf-8") as token:
                for access in token:
                    access = access.strip()
                    access_token = access"""

            r = s.post(
                'https://api-testing.ardoriguezf.es/{arodriguezf}',
                headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                         'Authorization': f'Bearer {ACCESS_TOKEN}'},
                json={
                    "contactPhone": "613223344"
                }
            )

        except:
            print("-------------------------------------------------")
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))

        else:
            if r.status_code == 200:
                print("-------------------------------------------------")
                print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))

        finally:
            print("\nEl reCaptcha hace que devuelva -> 403 Forbidden")
            print("-------------------------------------------------")

#
#
#
#
#######################
###  SUBSCRIPTIONS  ###
#######################
#
# GET -> /subscriptions
# GET -> /subscriptions/cards
# POST -> /subscriptions
# POST -> /subscriptions/extend/{clientId}
#
# Obtenemos las suscripciones que posee el cliente -> Z48poHG30hr1Wx5Sat6l
# GET -> https://api-testing.ardoriguezf.es/{arodriguezf}
# Get subscription client
#


class TestSubscriptions(unittest.TestCase):
    def test_16_get_subscriptions(self):
        print('\n\n**********  Subscriptions  **********')
        print('Getting Subscriptions')
        params = {
            'client': 'Z488h4SJG451Wx5Sat6l',
            'product': 'default'
        }
        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Creamos una nueva suscripcion -> En Firestore se visualiza en el mismo documento default
    # Si cambiamos el endDate, se vera como actualiza (crea) la suscripcion en cuestion
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Create subscription
    #

    def test_17_create_subscription(self):
        print('\nCreating Subscriptions')
        params = {
            'client': 'Z4TEF4SK0hr1Wx5Sat6l',
            'product': 'default',
            'stripeId': 'sub_1Mw1WLPOMyFxSIcSr2I46SlZ',
            'stripeCustomer': 'cus_NhQLkYTxfdKzyO',
            'stripeSession': "",
            'endDate': '2037-01-02T15:04:05Z'  # Podemos cambiar el mes o anio a modo de validacion
        }
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Extendemos suscripciones en cliente -> x8vmgAhxudLTEmLhcboC
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Extend a subscription
    #

    def test_18_extend_subscription(self):
        print('\nExtend Subscriptions')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
            json={
                "numLicensesToBeAdded": 1
            }
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Para obtener tarjetas del cliente -> 1HhPRdAzXYgzQWEui6H6
    # Primero generamos Bearer Token
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Obtain cards
    #

    def test_19_get_cards(self):
        print('\nGetting client cards')
        #
        # Obtain Bearer token
        #
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            json={
                "email": "abgrodriguezfarias@gmail.com",  # -> 1HhPRdAzXYgzQWEui6H6
                "password": "T3st.1234"
            }
        )

        token = r.json()
        ACCESS_TOKEN = token.get('data')  # Bearer token en variable ACCESS_TOKEN

        if r.status_code == 200:
            pass
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

        #
        #
        # getClientCards
        #

        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                     'Authorization': f'Bearer {ACCESS_TOKEN}'},
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

#
#
#
#
#################
###  Reports  ###
#################
#
# GET -> /reports/{domain
# GET -> /webreports/{domain}
#
# Obtenemos reporte de /client -> Tu nivel de ciberseguridad
# GET -> https://api-testing.ardoriguezf.es/{arodriguezf}
# Get report [SCORING]
#


class TestReports(unittest.TestCase):
    def test_20_report_scoring(self):
        print('\n\n**********  Reports  **********')
        print('Getting report - [SCORING]')
        params = {
            'email_at': 'arodriguezf.com'
        }
        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Obtenemos reporte de -> /client/websitesecurity
    # GET -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Get report [WEB]
    #

    def test_21_report_web(self):
        print('\nGetting report - [WEB]')
        params = {
            'email_at': 'arodriguezf.com'
        }
        r = s.get(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

#
#
#
#
########################
###  Security Scans  ###
########################
#
# POST -> /scans
# POST -> /scans/{domain}
#
# Escaneamos dominio WEB -> Es el VOLVER A ANALIZAR -> /client/websitesecurity
# POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
# Scan WEB domain
#


class TestSecurityScans(unittest.TestCase):
    def test_22_scan_web(self):
        print('\n\n**********  Security Scans  **********')
        print('Scanning domain - [WEB]')
        params = {
            'domain': 'arodriguezf.es'
        }
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 202:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

    #
    #
    #
    # Escaneamos dominio de correo -> Es el VOLVER A ANALIZAR -> /client/configure-email-security
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # Scan WEB domain
    #

    def test_23_scan_email(self):
        print('\nScanning domain - [eMail]')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 202:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()

#
#
#
#
##################
###  Breaches  ###
##################
#
# POST -> /breaches/dismiss
#
# Filtraciones de datos -> /client/data-alert
# POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
# Scan WEB domain
#


class TestBreaches(unittest.TestCase):
    def test_24_data_alert(self):
        print('\n\n**********  Breaches  **********')
        print('Breaches - Dismiss')
        params = {
            'email': 'abgrodriguezfarias@gmail.com',
            'client': 'pDDVQgmvbouD8rqHsVjy',
            'breach': 'stub breach',
            'date': '2036-01-02T15:04:05Z'
        }
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            params=params,
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()
#
#
#
#
###############
###  Leads  ###
###############
#
#
# POST -> /leads/api/v1/leads
# POST -> /leads/api/v1/bonus_kit
#
# Create Lead
# POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
# reCaptcha v3 is enabled
# 403 Forbidden is ok
#


class TestLeads(unittest.TestCase):
    def test_25_create_lead(self):
        print('\n\n**********  Leads  **********')
        print('Create Lead')
        try:
            r = s.post(
                'https://api-testing.ardoriguezf.es/{arodriguezf}',
                headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
                json={
                    "atEmail": "arodriguezf.com",
                    "company": {
                        "name": "T3st",
                        "numberEmployees": "10-49",
                        "sector": "Industrias extractivas",
                        "website": "arodriguezf.es"
                        },
                    "email": "test@gmail.com",
                    "eventName": "TEST Antonio Rodriguez",
                    "isEvent": True,
                    "language": "es",
                    "name": "Antonio Rodriguez",
                    "phone": "613223344"
                }
            )
        except:
            print("-------------------------------------------------")
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()
        else:
            if r.status_code == 201 or 403:
                print("-------------------------------------------------")
                print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
        finally:
            print("\nreCaptcha v3 -> 403 Forbidden")
            print("-------------------------------------------------")

    #
    #
    # Create Lead with Bonus Kit
    # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
    # reCaptcha v3 is enabled
    # 403 Forbidden is ok
    #

    def test_26_create_lead_bonus(self):
        try:
            print('\nCreate Lead with Bonus Kit')
            r = s.post(
                'https://api-testing.ardoriguezf.es/{arodriguezf}',
                headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}'},
                json={
                    "bono": {
                        "number": "123",
                        "date": "2023-03-07T12:39:45+00:00"
                    },
                    "company": {
                        "name": "test",
                        "website": "es.arodriguezf.tech",
                        "numberEmployees": "10-49",
                        "sector": "Actividades de organizaciones y organismos"
                    },
                    "name": "test",
                    "email": "antonio.rodriguez@outlook.es",
                    "phone": "613223344",
                    "eventName": "TEST Antonio Rodriguez",
                    "atEmail": "arodriguezf.es"
                }
            )
        except:
            print("-------------------------------------------------")
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()
        else:
            if r.status_code == 201 or 403:
                print("-------------------------------------------------")
                print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
        finally:
            print("\nreCaptcha v3 -> 403 Forbidden")
            print("-------------------------------------------------")
#
#
#
#############################
###  Qualification Forms  ###
#############################
#
#
# POST -> /forms/qualification/remind
# /forms/qualification/answers
# /forms/qualification/admin
#
# Send remind email for qualification form
# POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
#


class TestQualificationForms(unittest.TestCase):
    def test_27_remind_email_form(self):
        #
        # Cliente -> BmHXDMC6LoK5cJd0F9Kj
        # Primero generamos Bearer Token
        # POST -> https://api-testing.ardoriguezf.es/{arodriguezf}
        # Obtain token
        #
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
            json={
                "email": "abgrodriguezfarias@gmail.com",  # -> BmHXDMC6LoK5cJd0F9Kj
                "password": "T3st.1234"
            }
        )

        token = r.json()
        ACCESS_TOKEN = token.get('data')  # Bearer token en variable ACCESS_TOKEN

        if r.status_code == 200:
            pass
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()
        #
        #
        print('\nRemind eMail - Qualification Forms')
        r = s.post(
            'https://api-testing.ardoriguezf.es/{arodriguezf}',
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'x-api-key': f'{API_KEY}',
                     'Authorization': f'Bearer {ACCESS_TOKEN}'}
        )
        if r.status_code == 200:
            print("-------------------------------------------------")
            print(str(r.request) + "  " + str(r.status_code) + " " + r.reason + " in " + str(r.elapsed))
            print("-------------------------------------------------")
        else:
            print('[FAILED]  Ha devuelto -> {}'.format(r.status_code))
            sys.exit()


if __name__ == '__main__':
    unittest.main()

## Copyright (c) 2018 Denis Sacchet <denis@sacchet.fr>
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

import DomotApiModbus

class BoilerDedietrich(DomotApiModbus.Modbus):

    def __init__(
            self,
            Port,
            SlaveAddress = 0xA,
            Mode = 'rtu',
            Serial = {
                'baudrate':9600,
                'bytesize':8,
                'parity':'N',
                'stopbits':1
                }, 
            Timeout = 0.05):
        self._ITEMS={
                'software_version': {
                    'description':'software version',
                    'type':'holding_register',
                    'params':{'RegisterAddress':3,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'heure': {
                    'description':'Date : heure',
                    'type':'holding_register',
                    'params':{'RegisterAddress':4,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'minute': {
                    'description':'Date : minute',
                    'type':'holding_register',
                    'params':{'RegisterAddress':5,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'jour_semaine': {
                    'description':'Date: Jour de la semaine : 1 => lundi .... 7 => dimanche',
                    'type':'holding_register',
                    'params':{'RegisterAddress':6,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_exterieure': { 
                    'description':'outdoor sensor',
                    'type':'holding_register',
                    'params':{'RegisterAddress':7,'NumberOfDecimals':1,'Signed':True},
                    'actions':('get')
                    },
                'temperature_ete_hiver': { 
                    'description':'Summer/winter setpoint',
                    'type':'holding_register',
                    'params':{'RegisterAddress':8,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'hors_gel_exterieure': { 
                    'description':'Outdoor temperature setpoint activating the installation antifreeze',
                    'type':'holding_register',
                    'params':{'RegisterAddress':9,'NumberOfDecimals':1,'Signed':True},
                    'actions':('get')
                    },
                'nuit_arret_abaissement': { 
                    'description':'Night decrease or Night stop mode',
                    'type':'holding_register',
                    'params':{'RegisterAddress':10,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'tempo_pompe_chauffage': { 
                    'description':'heating pump Postrun',
                    'type':'holding_register',
                    'params':{'RegisterAddress':11,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'auto_adaptation': { 
                    'description':'Heat Curves auto adaptative mode (Only if room sensor present)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':12,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'temperature_jour_a': {
                    'description':'Day Room temperature setpoint Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':14,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },                
                'temperature_nuit_a': {
                    'description':'Night Room temperature setpoint Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':15,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_antigel_a': {
                    'description':'Antifreeze room temperature setpoint circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':16,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'derogation_a_dhw': {
                    'description':'Derog A+DHW',
                    'type':'holding_register',
                    'decode':self.DecodeDerogation,
                    'params':{'RegisterAddress':17,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_ambiance_a': {
                    'description':'room temperature Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':18,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'influence_sonde_ambiance_a': {
                    'description':'Room sensor Heating influence Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':19,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'pente_a': {
                    'description':'Heat curve Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':20,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_calculee_a': {
                    'description':'Calculated Setpoint Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':21,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'temperature_jour_b': {
                    'description':'Day Room temperature setpoint Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':23,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },                
                'temperature_nuit_b': {
                    'description':'Night Room temperature setpoint Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':24,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_antigel_b': {
                    'description':'Bntifreeze room temperature setpoint circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':25,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'derogation_b_dhw': {
                    'description':'Derog B+DHW',
                    'type':'holding_register',
                    'params':{'RegisterAddress':26,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_ambiance_b': {
                    'description':'room temperature Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':27,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'influence_sonde_ambiance_b': {
                    'description':'Room sensor Heating influence Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':28,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'pente_b': {
                    'description':'Heat curve Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':29,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_maxi_circuit_b': {
                    'description':'Maximun temp Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':31,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'temperature_calculee_b': {
                    'description':'Calculated Setpoint Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':32,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'temperature_jour_c': {
                    'description':'Day Room temperature setpoint Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':35,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },                
                'temperature_nuit_c': {
                    'description':'Night Room temperature setpoint Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':36,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_antigel_c': {
                    'description':'Bntifreeze room temperature setpoint circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':37,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'derogation_c_dhw': {
                    'description':'Derog C+DHW',
                    'type':'holding_register',
                    'params':{'RegisterAddress':38,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_ambiance_c': {
                    'description':'room temperature Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':39,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'influence_sonde_ambiance_c': {
                    'description':'Room sensor Heating influence Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':40,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'pente_c': {
                    'description':'Heat curve Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':41,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_maxi_circuit_c': {
                    'description':'Maximun temp Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':43,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'temperature_calculee_c': {
                    'description':'Calculated Setpoint Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':44,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'mesure_depart_c': {
                    'description':'Outlet temperature Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':45,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'temperature_ballon_jour': {
                    'description':'DHW temperature Day Setpoint',
                    'type':'holding_register',
                    'params':{'RegisterAddress':59,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'priorite_ecs': {
                    'description':'DHW Priority',
                    'mapping':{ 0:'total',1:'sliding',2:'no priority'},
                    'type':'holding_register',
                    'params':{'RegisterAddress':60,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'tempo_pompe_ecs': {
                    'description':'DHW pump postrun',
                    'type':'holding_register',
                    'params':{'RegisterAddress':61,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_ballon': {
                    'description':'DHW Temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':62,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get')
                    },
                'permutation_cascade': {
                    'description':'Permutation (cascade)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':63,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'chaudiere_pilote_cascade': {
                    'description':'Leading boiler (cascade)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':64,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'temperature_calculee_chaudiere': {
                    'description':'Boiler Calculated Setpoint',
                    'type':'holding_register',
                    'params':{'RegisterAddress':74,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'mesure_temprature_conduit_chaudiere_mit': {
                    'description':'Boiler/MIT Flue Temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':75,'NumberOfDecimals':1,'Signed':True},
                    'actions':('get')
                    },
                'nombre_impulsions_bruleur_x10': {
                    'description':'Numbers of Burner starts (X10)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':77,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'nombre_heure_bruleur_x10': {
                    'description':'Burner operating hours (X10)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':78,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'temperature_ballon_nuit': {
                    'description':'DHW temperature Night Setpoint',
                    'type':'holding_register',
                    'params':{'RegisterAddress':96,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_exterieure_moyenne': {
                    'description':'Average outdoot temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':102,'NumberOfDecimals':1,'Signed':True},
                    'actions':('get')
                    },
                'nombre_d_allures': {
                    'description':'Number of Stages operating',
                    'type':'holding_register',
                    'params':{'RegisterAddress':103,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'jour': {
                    'description':'Date : jour (1..31)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':108,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'mois': {
                    'description':'Date : mois (1..12)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':109,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'annee': {
                    'description':'Date: Annee (0..99)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':110,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'temperature_primare_ecs': {
                    'description':'Boiler temperature Setpoint for DHW production',
                    'type':'holding_register',
                    'params':{'RegisterAddress':121,'NumberOfDecimals':1,'Signed':False},
                    'actions':('get','put')
                    },
                'langue': {
                    'description':'Language',
                    'mapping':{ 0:'French',1:'German',2:'English',3:'Italiano',4:'Spanish',5:'Netherland',6:'Polsky',7:'Turquish',8:'Russian'},
                    'type':'holding_register',
                    'params':{'RegisterAddress':263,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'inertie_batiment': {
                    'description':'Building inertia',
                    'type':'holding_register',
                    'params':{'RegisterAddress':264,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'-','type':'integer','min':0,'max':10},
                    'actions':('get','put')
                    },
                'decalage_temperature_chaudiere_v3v': {
                    'description':'Temperature Shift between Boiler and 3-Way Valve',
                    'type':'holding_register',
                    'params':{'RegisterAddress':267,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'K','type':'float','min':0,'max':16},
                    'actions':('get','put')
                    },
                'antilegionellose': {
                    'description':'Configuration of the legionnella protection',
                    'type':'holding_register',
                    'mapping':{ 0:'none',1:'daily',2:'weekly'},
                    'params':{'RegisterAddress':268,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':2},
                    'actions':('get','put')
                    },
                'fonctionnement_minimum_bruleur': {
                    'description':'Minimum burner operating time',
                    'type':'holding_register',
                    'params':{'RegisterAddress':269,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'sec','type':'integer','min':10,'max':180},
                    'actions':('get','put')
                    },
                'tempo_pompe_chaudiere': {
                    'description':'Boiler Pump Postrun',
                    'type':'holding_register',
                    'params':{'RegisterAddress':272,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'min','type':'integer','min':1,'max':99},
                    'actions':('get','put')
                    },
                'calibration_exterieure': {
                    'description':'Outside temperature calibration',
                    'type':'holding_register',
                    'params':{'RegisterAddress':274,'NumberOfDecimals':1,'Signed':True},
                    'constraints':{'units':'C','type':'float','min':-5,'max':5},
                    'actions':('get','put')
                    },
                'calibration_ambiance_a': {
                    'description':'Room temperature calibration Circ A',
                    'type':'holding_register',
                    'params':{'RegisterAddress':275,'NumberOfDecimals':1,'Signed':True},
                    'constraints':{'units':'C','type':'float','min':-5.0,'max':5.0},
                    'actions':('get','put')
                    },
                'calibration_ambiance_b': {
                    'description':'Room temperature calibration Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':276,'NumberOfDecimals':1,'Signed':True},
                    'constraints':{'units':'C','type':'float','min':-5.0,'max':5.0},
                    'actions':('get','put')
                    },
                'calibration_ambiance_c': {
                    'description':'Room temperature calibration Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':277,'NumberOfDecimals':1,'Signed':True},
                    'constraints':{'units':'C','type':'float','min':-5.0,'max':5.0},
                    'actions':('get','put')
                    },
                'anticipation_a': {
                    'description':'Activation and adjustement of the anticipation time Circ A / 10.1 => no',
                    'type':'holding_register',
                    'params':{'RegisterAddress':282,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'DH','type':'float','min':0.0,'max':10.1},
                    'actions':('get','put')
                    },
                'anticipation_b': {
                    'description':'Activation and adjustement of the anticipation time Circ B / 10.1 => no',
                    'type':'holding_register',
                    'params':{'RegisterAddress':283,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'DH','type':'float','min':0.0,'max':10.1},
                    'actions':('get','put')
                    },
                'anticipation_c': {
                    'description':'Activation and adjustement of the anticipation time Circ C / 10.1 => no',
                    'type':'holding_register',
                    'params':{'RegisterAddress':284,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'DH','type':'float','min':0.0,'max':10.1},
                    'actions':('get','put')
                    },
                'tpc_j_a': {
                    'description':'Day heat curve footpoint Circ A / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':289,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'tpc_n_a': {
                    'description':'Night heat curve footpoint Circ A / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':290,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'tpc_j_b': {
                    'description':'Day heat curve footpoint Circ B / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':291,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'tpc_n_b': {
                    'description':'Night heat curve footpoint Circ B / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':292,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'type_circ_a': {
                    'description':'Circuit A type',
                    'type':'holding_register',
                    'mapping':{ 0:'disable',1:'direct',2:'na',3:'na',4:'na',5:'program',6:'na',7:'h_temp',8:'na',9:'na',10:'na',11:'dhw',12:'na',13:'na',14:'na',15:'electrical_dhw'},
                    'params':{'RegisterAddress':296,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':15},
                    'actions':('get','put')
                    },
                'type_circ_b': {
                    'description':'Circuit B type',
                    'type':'holding_register',
                    'mapping':{ 0:'na',1:'direct',2:'3wv',3:'na',4:'swimming_pool'},
                    'params':{'RegisterAddress':296,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':4},
                    'actions':('get','put')
                    },
                'temperature_maxi_circuit_a': {
                    'description':'Maximun temp Circ A', 
                    'type':'holding_register',
                    'params':{'RegisterAddress':299,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':30.0,'max':95.0,'step':1.0},
                    'actions':('get','put')
                    },
                'type_entree_systeme': {
                    'description':'Function of the system input',
                    'mapping':{ 0:'disable',1:'system',2:'storage_tank',3:'dhw_strat',4:'storage_tank_+_dhw'},
                    'type':'holding_register',
                    'params':{'RegisterAddress':303,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':4,'step':1},
                    'actions':('get','put')
                    },
                'vitesse_max_ventilateur': {
                    'description':'Maximum fan speed',
                    'type':'holding_register',
                    'params':{'RegisterAddress':305,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'rev/min','type':'integer','min':0,'max':10000,'step':100},
                    'actions':('get')
                    },
                'vitesse_ventilateur': {
                    'description':'Current fan speed',
                    'type':'holding_register',
                    'params':{'RegisterAddress':307,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'rev/min','type':'integer','min':0,'max':10000,'step':1},
                    'actions':('get')
                    },
                'tpc_j_c': {
                    'description':'Day heat curve footpoint Circ C / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':358,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'tpc_n_c': {
                    'description':'Night heat curve footpoint Circ C / 15.0 => no (function inactive)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':359,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':15.0,'max':90.0},
                    'actions':('get','put')
                    },
                'type_circ_c': {
                    'description':'Circuit C type',
                    'type':'holding_register',
                    'mapping':{ 0:'na',1:'direct',2:'3wv',3:'na',4:'swimming_pool'},
                    'params':{'RegisterAddress':360,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':4},
                    'actions':('get','put')
                    },
                'mesure_pression_eau': {
                    'description':'water_pressure',
                    'type':'holding_register',
                    'params':{'RegisterAddress':437,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'Bar','type':'float','min':0.0,'max':10.0,'step':0.1},
                    'actions':('get')
                    },
                'largeur_bande_v3v': {
                    'description':'3WV bandwidth',
                    'type':'holding_register',
                    'params':{'RegisterAddress':438,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'K','type':'float','min':4.0,'max':16.0,'step':1.0},
                    'actions':('get','put')
                    },
                'mesure_courant_ionisation': {
                    'description':'Ionization current',
                    'type':'holding_register',
                    'params':{'RegisterAddress':451,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'uA','type':'float','min':0.0,'max':50.0,'step':0.1},
                    'actions':('get')
                    },
                'puissance_instantannee_oth': {
                    'description':'Instantaneous power only on oth/modbus interface',
                    'type':'holding_register',
                    'params':{'RegisterAddress':458,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'%','type':'integer','min':0,'max':100,'step':1},
                    'actions':('get')
                    },
                'defaut_chaudiere': {
                    'description':'boiler failure',
                    'type':'holding_register',
                    'mapping': {
                        '0x0':'D3:OUTL S.B FAIL.',
                        '0x1':'D4:OUTL S.C FAIL.',
                        '0x2':'D5:OUTSI.S.FAIL.',
                        '0x3':'D7:SYST.SENS.FAIL.',
                        '0x4':'D9:DHW S.FAILURE',
                        '0x5':'D11:ROOM S.A FAIL.',
                        '0x6':'D12:ROOM S.B FAIL.',
                        '0x7':'D13:ROOM S.C FAIL.',
                        '0x8':'D14:MC COM.FAIL',
                        '0x9':'D15:ST.TANK S.FAIL',
                        '0xA':'D16:SWIM.P.B.S.FA',
                        '0xB':'D16:SWIM.P.C.S.FA',
                        '0xC':'D17:DHW 2 S.FAIL',
                        '0xD':'D27:PCU COM.FAIL',
                        '0xE':'Not Available',
                        '0xF':'Not Available',
                        '0x10':'Not Available',
                        '0x11':'Not Available',
                        '0x12':'D32:5 RESET:ON/OFF',
                        '0x13':'D37:TA-S SHORT-CIR',
                        '0x14':'D38:TA-S DISCONNEC',
                        '0x15':'D39:TA-S FAILURE',
                        '0x16':'D50:OTH COM.FAIL',
                        '0x17':'D51:DEF :SEE BOILER',
                        '0x18':'D18:SOL.HW S.FAIL',
                        '0x19':'D19:SOL.COL.S.FAIL',
                        '0x1A':'D20:SOL COM.FAIL',
                        '0x1B':'D99:DEF.BAD PCU',
                        '0x1C':'D40:FAIL UNKNOWN',
                        '0x1D':'D254:FAIL UNKNOWN',
                        '0x800':'B0:PSU FAIL',
                        '0x801':'B1:PSU PARAM FAIL',
                        '0x802':'B2:EXCHAN.S.FAIL',
                        '0x803':'B3:EXCHAN.S.FAIL',
                        '0x804':'B4:EXCHAN.S.FAIL',
                        '0x805':'B5:STB EXCHANGE',
                        '0x806':'B6:BACK S.FAILURE',
                        '0x807':'B7:BACK S.FAILURE',
                        '0x808':'B8:BACK S.FAILURE',
                        '0x809':'B9:STB BACK',
                        '0x80A':'B10:DT.EXCH.BAC.FAIL',
                        '0x80B':'B11:DT.BAC.EXCH.FAIL',
                        '0x80C':'B12:STB OPEN',
                        '0x80D':'B14:BURNER FAILURE',
                        '0x80E':'B15:CCE.TST.FAIL',
                        '0x80F':'B16:PARASIT FLAME',
                        '0x810':'B17:VALVE FAIL',
                        '0x811':'B32:DEF.OUTLET S.',
                        '0x812':'B33:DEF.OUTLET S.',
                        '0x813':'B34:FAN FAILURE',
                        '0x814':'B35:BACK>BOIL FAIL',
                        '0x815':'B36:I-CURRENT FAIL',
                        '0x816':'B37:SU COM.FAIL',
                        '0x817':'B38:PCU COM.FAIL',
                        '0x818':'B39:BL OPEN FAIL',
                        '0x819':'B255:FAIL UNKNOWN',
                        '0x81A':'B254:FAIL UNKNOWN',
                        '0x1000':'DEF.PSU 00',
                        '0x1001':'DEF.PSU PARAM 01',
                        '0x1002':'DEF.S.DEPART 02',
                        '0x1003':'DEF.S.DEPART 03',
                        '0x1004':'DEF.S.DEPART 04',
                        '0x1005':'STB DEPART 05',
                        '0x1006':'DEF.S.RETOUR 06',
                        '0x1007':'DEF.S.RETOUR 07',
                        '0x1008':'DEF.S.RETOUR 08',
                        '0x1009':'STB RETOUR 09',
                        '0x100A':'DT.DEP-RET<MIN 10',
                        '0x100B':'DT.DEP-RET>MAX 11',
                        '0x100C':'STB OUVERT 12',
                        '0x100D':'DEF.ALLUMAGE 14',
                        '0x100E':'FLAM.PARASI. 16',
                        '0x100F':'DEF.VANNE GAZ 17',
                        '0x1010':'DEF.VENTILO 34',
                        '0x1011':'DEF.RET>CHAUD 35',
                        '0x1012':'DEF.IONISATION 36',
                        '0x1013':'DEF.COM.SU 37',
                        '0x1014':'DEF.COM PCU 38',
                        '0x1015':'DEF BL OUVERT 39',
                        '0x1016':'DEF.TEST.HRU 40',
                        '0x1017':'DEF.MANQUE EAU 250',
                        '0x1018':'DEF.MANOMETRE 251',
                        '0x1019':'DEF.INCONNU 255',
                        '0x101A':'DEF.INCONNU 254',
                        '0x1800':'L0:PSU FAIL',
                        '0x1801':'L1:PSU PARAM FAIL',
                        '0x1802':'L2:STB OUTLET',
                        '0x1803':'L3:DEF.OIL.SENSOR',
                        '0x1804':'L4:BURNER FAILURE',
                        '0x1805':'L5:DEF.INTERNAL',
                        '0x1806':'L6:DEF.SPEED.MOT',
                        '0x1807':'L7:DEF.T.WARM UP',
                        '0x1808':'L8:DEF.PAR.FLAME',
                        '0x1809':'L9:OIL.PRES FAIL.',
                        '0x180A':'L30:SMOKE PRE.FAIL',
                        '0x180B':'L31:DEF.SMOKE.TEMP',
                        '0x180C':'L32:DEF.OUTLET S.',
                        '0x180D':'L33:DEF.OUTLET S.',
                        '0x180E':'L34:BACK S.FAILURE',
                        '0x180F':'L35:BACK S.FAILURE',
                        '0x1810':'L36:DEF.FLAME LOS',
                        '0x1811':'L37:SU COM.FAIL',
                        '0x1812':'L38:PCU COM.FAIL',
                        '0x1813':'L39:BL OPEN FAIL',
                        '0x1814':'L250:DEF.WATER MIS.',
                        '0x1815':'L251:MANOMETRE FAIL',
                        '0x1816':'L255:FAIL UNKNOWN',
                        '0x1817':'L254:FAIL UNKNOWN',
                        '0x2000':'L1:DEF.COMP.PAC',
                        '0x2001':'L2:DEF.V4V PAC',
                        '0x2002':'L3:DEF.POMPE PAC',
                        '0x2003':'L4:PAC HORS LIMIT',
                        '0x2004':'L5:DEF.DEB.PAC 6',
                        '0x2005':'L6:DEF.DEB.PAC 8',
                        '0x2006':'L7:DEF.COM.PAC',
                        '0x2007':'L8:DEF.S.SOR.COMP',
                        '0x2008':'L9:DEF.H.P PAC',
                        '0x2009':'L10:DEF.B.P PAC',
                        '0x200A':'L11:DEF.PRES.SOURC',
                        '0x200B':'L12:DEF.ANTI.SOUR.',
                        '0x200C':'L13:DEF.P.SOURCE',
                        '0x200D':'L14:DEF.ANTI.COND.',
                        '0x200E':'L15:DEF.DEGIVRAGE',
                        '0x200F':'L16:DEF.PROT.MOT.',
                        '0x2010':'L17:DEF.S.GAZ.CH.',
                        '0x2011':'L18:DEF.COM.PAC',
                        '0x2012':'L19:DEF.S.DEP.PAC',
                        '0x2013':'L20:DEF.S.RET.PAC',
                        '0x2014':'L21:DEF.S.EXT.ENT.',
                        '0x2015':'L22:DEF.S.EXT.SOR.',
                        '0x2016':'L23:DEF.S.GAZ EXP.',
                        '0x2017':'L24:DEF.S.EVAPO.',
                        '0x2018':'L25:DEF.S.CONDENS.',
                        '0x2019':'L32:BL.USER.RESET',
                        '0x201A':'L33:DEF.DEBIT',
                        '0x201B':'L255:DEF.INCONNU',
                        '0x201C':'L254:DEF.INCONNU',
                        '0xffff':'No failure'
                    },
                    'params':{'RegisterAddress':465,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':65535,'step':1},
                    'actions':('get')
                    },
                'puissance_instantannee': {
                    'description':'Instantaneous power',
                    'type':'holding_register',
                    'params':{'RegisterAddress':471,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'%','type':'integer','min':0,'max':100,'step':1},
                    'actions':('get')
                    },
                'nombre_allure_bruleur': {
                    'description':'Nb burner stage',
                    'type':'holding_register',
                    'params':{'RegisterAddress':473,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':3,'step':1},
                    'actions':('get')
                    },
                'primary_output_states': {
                    'description':'Primary Output States',
                    'type':'holding_register',
                    'decode':self.DecodePrimaryOutputStates,
                    'params':{'RegisterAddress':474,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'secondary_output_states': {
                    'description':'Secondary Output States',
                    'type':'holding_register',
                    'decode':self.DecodeSecondaryOutputStates,
                    'params':{'RegisterAddress':475,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'alarme': {
                    'description':'Failure',
                    'type':'holding_register',
                    'mapping':{ 0:'no_failure',1:'failure'},
                    'params':{'RegisterAddress':500,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':1,'step':1},
                    'actions':('get')
                    },
                'mesure_temperature_retour': {
                    'description':'Boiler return temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':607,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':150.0,'step':0.1},
                    'actions':('get')
                    },
                'mesure_temperature_systeme': {
                    'description':'System temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':622,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':150.0,'step':0.1},
                    'actions':('get')
                    },
                'mesure_temperature_echangeur': {
                    'description':'Heat exchanger temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':625,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':150.0,'step':0.1},
                    'actions':('get')
                    },
                'mesure_moyenne_mit_pac': {
                    'description':'average flow sensor temperature (HP only)',
                    'type':'holding_register',
                    'params':{'RegisterAddress':629,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':150.0,'step':0.1},
                    'actions':('get')
                    },
                'mesure_0_10v': {
                    'description':'measure 0-10V voltage input',
                    'type':'holding_register',
                    'params':{'RegisterAddress':634,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'V','type':'float','min':0.0,'max':15.0,'step':0.1},
                    'actions':('get')
                    },
                'mode_fonctionnement_circuit_a': {
                    'description':'Heating mode Circ A',
                    'type':'holding_register',
                    'mapping':{ 0:'antifreeze',2:'night',4:'day'},
                    'params':{'RegisterAddress':637,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'mode_fonctionnement_circuit_b': {
                    'description':'Heating mode Circ B',
                    'type':'holding_register',
                    'mapping':{ 0:'antifreeze',2:'night',4:'day'},
                    'params':{'RegisterAddress':638,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'mode_fonctionnement_circuit_c': {
                    'description':'Heating mode Circ C',
                    'type':'holding_register',
                    'mapping':{ 0:'antifreeze',2:'night',4:'day'},
                    'params':{'RegisterAddress':639,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'mode_fonctionnement_dhw': {
                    'description':'Heating mode DHW',
                    'type':'holding_register',
                    'mapping':{ 0:'antifreeze',2:'night',4:'day'},
                    'params':{'RegisterAddress':640,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'mode_fonctionnement_aux': {
                    'description':'Heating mode Aux',
                    'type':'holding_register',
                    'mapping':{ 0:'antifreeze',2:'night',4:'day'},
                    'params':{'RegisterAddress':641,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'mode_fonctionnement_chaudiere': {
                    'description':'Summer/Winter mode',
                    'type':'holding_register',
                    'mapping':{ 4:'summer',5:'winter'},
                    'params':{'RegisterAddress':644,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0,'max':255,'step':1},
                    'actions':('get')
                    },
                'maximum_chaudiere': {
                    'description':'Maximum boiler temperature',
                    'type':'holding_register',
                    'params':{'RegisterAddress':678,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':20.0,'max':95.0,'step':1.0},
                    'actions':('get')
                    },
                'consigne_piscine_b': {
                    'description':'Swimming pool temperature setpoint Circ B',
                    'type':'holding_register',
                    'params':{'RegisterAddress':686,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':39.0,'step':5},
                    'actions':('get','put')
                    },
                'consigne_piscine_c': {
                    'description':'Swimming pool temperature setpoint Circ C',
                    'type':'holding_register',
                    'params':{'RegisterAddress':687,'NumberOfDecimals':1,'Signed':False},
                    'constraints':{'units':'C','type':'float','min':0.0,'max':39.0,'step':5},
                    'actions':('get','put')
                    },
                'hp_states': {
                    'description':'HP States if MIT/MHR',
                    'type':'holding_register',
                    'decode':self.DecodeHpStates,
                    'params':{'RegisterAddress':707,'NumberOfDecimals':0,'Signed':False},
                    'constraints':{'units':'na','type':'integer','min':0.0,'max':39.0,'step':5},
                    'actions':('get')
                    },
                'boiler_states': {
                    'description':'Boiler states',
                    'type':'holding_register',
                    'decode':self.DecodeBoilerStates,
                    'params':{'RegisterAddress':735,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'compteur_energie': {
                    'description':'Energy counter',
                    'type':'holding_register',
                    'params':{'RegisterAddress':787,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get','put')
                    },
                'consommation_chauffage_MWh': {
                    'description':'',
                    'type':'holding_register',
                    'params':{'RegisterAddress':788,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'consommation_chauffage_kWh': {
                    'description':'',
                    'type':'holding_register',
                    'params':{'RegisterAddress':789,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                'consommation_chauffage_Wh': {
                    'description':'',
                    'type':'holding_register',
                    'params':{'RegisterAddress':790,'NumberOfDecimals':0,'Signed':False},
                    'actions':('get')
                    },
                }
        super(BoilerDedietrich,self).__init__(Port = Port,SlaveAddress = SlaveAddress,Mode = Mode,Serial = Serial, Timeout = Timeout)
        self.SetRetryStopMaxAttemptNumber(60)
        self.SetRetryWaitFixed(1000)

    def DecodeDerogation(self, Value):
        result = dict()
        # circ derog all # 0=only current circuit # 1=all circuit
        if(Value&0b10000000):
            result['circ_derog_all']=1
        else:
            result['circ_derog_all']=0
        # DHW derog type # 0= 7/7 # 1=until end time program
        if(Value&0b01000000):
            result['dwh_derog_type']=1
        else:
            result['dwh_derog_type']=0
        # Circ derog type # 0= 7/7 # 1=until end time program
        if(Value&0b00100000):
            result['circ_derog_type']=1
        else:
            result['circ_derog_type']=0
        # 1=DHW
        if(Value&0b00010000):
            result['dhw']=1
        else:
            result['dhw']=0
        # 1=AUTO
        if(Value&0b00001000):
            result['auto']=1
        else:
            result['auto']=0
        # 1=DAY
        if(Value&0b00000100):
            result['day']=1
        else:
            result['day']=0
        # 1=NIGHT
        if(Value&0b00000010):
            result['night']=1
        else:
            result['night']=0
        # 1=ANTIFREEZE
        if(Value&0b00000001):
            result['antifreeze']=1
        else:
            result['antifreeze']=0
        return result

    def EncodeDerogation(self, Value):
        result=0
        # circ derog all # 0=only current circuit # 1=all circuit
        if 'circ_derog_all' in Value and Value['circ_derog_all']:
            result=result|0b10000000
        # DHW derog type # 0= 7/7 # 1=until end time program
        if 'dwh_derog_type' in Value and Value['dwh_derog_type']:
            result=result|0b01000000
        # Circ derog type # 0= 7/7 # 1=until end time program
        if 'circ_derog_type' in Value and Value['circ_derog_type']:
            result=result|0b00100000
        # 1=DHW
        if 'dwh' in Value and Value['dwh']:
            result=result|0b00010000
        # 1=AUTO
        if 'auto' in Value and Value['auto']:
            result=result|0b00001000
        # 1=DAY
        if 'day' in Value and Value['day']:
            result=result|0b00000100
        # 1=NIGHT
        if 'night' in Value and Value['night']:
            result=result|0b00000010
        # 1=ANTIFREEZE
        if 'antifreeze' in Value and Value['antifreeze']:
            result=result|0b00000001
        return result

    def DecodePrimaryOutputStates(self,Value):
        result = dict()
        # Boiler pump
        if(Value&0b00010000):
            result['boiler_pump']=1
        else:
            result['boiler_pump']=0
        # Hydraulic valve close
        if(Value&0b00001000):
            result['hydraulic_valve_close']=1
        else:
            result['hydraulic_valve_close']=0
        # Hydraulic valve open
        if(Value&0b00000100):
            result['hydraulic_valve_open']=1
        else:
            result['hydraulic_valve_open']=0
        # Burner 1,2
        if(Value&0b00000010):
            result['burner_1_2']=1
        else:
            result['burner_1_2']=0
        # Burner 1,1
        if(Value&0b00000001):
            result['burner_1_1']=1
        else:
            result['burner_1_1']=0
        return result

    def DecodeSecondaryOutputStates(self,Value):
        result = dict()
        # bit15
        #if(Value&0b1000000000000000):
        #    result['bit15']=1
        #else:
        #    result['bit15']=0
        # bit14
        #if(Value&0b0100000000000000):
        #    result['bit14']=1
        #else:
        #    result['bit14']=0
        # bit13 Phone output
        if(Value&0b0010000000000000):
            result['phone_output']=1
        else:
            result['phone_output']=0
        # bit12
        #if(Value&0b0001000000000000):
        #    result['bit12']=1
        #else:
        #    result['bit12']=0
        # bit11
        #if(Value&0b0000100000000000):
        #    result['bit11']=1
        #else:
        #    result['bit11']=0
        # bit10 Aux Pump On
        if(Value&0b0000010000000000):
            result['aux_pump_on']=1
        else:
            result['aux_pump_on']=0
        # bit9 Circ C 3WV Close
        if(Value&0b0000001000000000):
            result['circ_c_3wv_close']=1
        else:
            result['circ_c_3wv_close']=0
        # bit8 Circ C 3WV Open
        if(Value&0b0000000100000000):
            result['circ_c_3wv_open']=1
        else:
            result['circ_c_3wv_open']=0
        # bit7 Circ C Pump On
        if(Value&0b0000000010000000):
            result['circ_c_pump_on']=1
        else:
            result['circ_c_pump_on']=0
        # bit6 Circ B 3WV Close
        if(Value&0b0000000001000000):
            result['circ_b_3wv_close']=1
        else:
            result['circ_b_3wv_close']=0
        # bit5 Circ B 3WV Open
        if(Value&0b0000000000100000):
            result['circ_b_3wv_open']=1
        else:
            result['circ_b_3wv_open']=0
        # bit4 Circ B Pump On
        if(Value&0b0000000000010000):
            result['circ_b_pump_on']=1
        else:
            result['circ_b_pump_on']=0
        # bit3
        #if(Value&0b0000000000001000):
        #    result['bit3']=1
        #else:
        #    result['bit3']=0
        # bit2
        #if(Value&0b0000000000000100):
        #    result['bit2']=1
        #else:
        #    result['bit2']=0
        # bit1 : Circ A Pump On
        if(Value&0b0000000000000010):
            result['circ_a_pump_on']=1
        else:
            result['circ_a_pump_on']=0
        # bit0 : DHW Pump On
        if(Value&0b0000000000000001):
            result['dwh_pump_on']=1
        else:
            result['dwh_pump_on']=0

        return result

    def DecodeHpStates(self,Value):
        result = dict()
        # bit15 compressor
        if(Value&0b1000000000000000):
            result['compressor']=1
        else:
            result['compressor']=0
        # bit14
        #if(Value&0b0100000000000000):
        #    result['bit14']=1
        #else:
        #    result['bit14']=0
        # bit13
        #if(Value&0b0010000000000000):
        #    result['bit13']=1
        #else:
        #    result['bit13']=0
        # bit12 Backup 1
        if(Value&0b0001000000000000):
            result['backup1']=1
        else:
            result['backup1']=0
        # bit11 Backup 2
        if(Value&0b0000100000000000):
            result['backup2']=1
        else:
            result['backup2']=0
        # bit10
        #if(Value&0b0000010000000000):
        #    result['bit10']=1
        #else:
        #    result['bit10']=0
        # bit9 
        #if(Value&0b0000001000000000):
        #    result['bit9']=1
        #else:
        #    result['bit9']=0
        # bit8 HP Pump
        if(Value&0b0000000100000000):
            result['hp_pump']=1
        else:
            result['hp_pump']=0
        # bit7
        #if(Value&0b0000000010000000):
        #    result['bit7']=1
        #else:
        #    result['bit7']=0
        # bit6
        #if(Value&0b0000000001000000):
        #    result['bit6']=1
        #else:
        #    result['bit6']=0
        # bit5 Boiler backup
        if(Value&0b0000000000100000):
            result['boiler_backup']=1
        else:
            result['boiler_backup']=0
        # bit4 boiler pump backup
        if(Value&0b0000000000010000):
            result['boiler_pump_backup']=1
        else:
            result['boiler_pump_backup']=0
        # bit3
        #if(Value&0b0000000000001000):
        #    result['bit3']=1
        #else:
        #    result['bit3']=0
        # bit2
        #if(Value&0b0000000000000100):
        #    result['bit2']=1
        #else:
        #    result['bit2']=0
        # bit1 : Defrosting
        if(Value&0b0000000000000010):
            result['defrosting']=1
        else:
            result['defrosting']=0
        # bit0
        #if(Value&0b0000000000000001):
        #    result['bit0']=1
        #else:
        #    result['bit0']=0

        return result

    def DecodeBoilerStates(self,Value):
        result = dict()
        # bit15 cascade failure
        if(Value&0b1000000000000000):
            result['cascade_failure']=1
        else:
            result['cascade_failure']=0
        # bit14
        #if(Value&0b0100000000000000):
        #    result['bit14']=1
        #else:
        #    result['bit14']=0
        # bit13
        #if(Value&0b0010000000000000):
        #    result['bit13']=1
        #else:
        #    result['bit13']=0
        # bit12
        #if(Value&0b0001000000000000):
        #    result['bit12']=1
        #else:
        #    result['bit12']=0
        # bit11
        #if(Value&0b0000100000000000):
        #    result['bit11']=1
        #else:
        #    result['bit11']=0
        # bit10
        #if(Value&0b0000010000000000):
        #    result['bit10']=1
        #else:
        #    result['bit10']=0
        # bit9 
        #if(Value&0b0000001000000000):
        #    result['bit9']=1
        #else:
        #    result['bit9']=0
        # bit8
        #if(Value&0b0000000100000000):
        #    result['bit8']=1
        #else:
        #    result['bit8']=0
        # bit7
        #if(Value&0b0000000010000000):
        #    result['bit7']=1
        #else:
        #    result['bit7']=0
        # bit6
        #if(Value&0b0000000001000000):
        #    result['bit6']=1
        #else:
        #    result['bit6']=0
        # bit5 Maximum possible output power
        if(Value&0b0000000000100000):
            result['maximum_possible_output_power']=1
        else:
            result['maximum_possible_output_power']=0
        # bit4 burner on
        if(Value&0b0000000000010000):
            result['burner_on']=1
        else:
            result['burner_on']=0
        # bit3 secondary pump
        if(Value&0b0000000000001000):
            result['secondary_pump']=1
        else:
            result['secondary_pump']=0
        # bit2 3Wv Circuit OFF
        if(Value&0b0000000000000100):
            result['3wv_circuit_off']=1
        else:
            result['3wv_circuit_off']=0
        # bit1 : Direct Circuit OFF
        if(Value&0b0000000000000010):
            result['direct_circuit_off']=1
        else:
            result['direct_circuit_off']=0
        # bit0
        #if(Value&0b0000000000000001):
        #    result['bit0']=1
        #else:
        #    result['bit0']=0

        return result

#    def WaitForSilence(self):
#        ser = serial.Serial(self.Port,self.Serial['baudrate'],timeout=1)
#        try:
#            ser.read(1)
#        except SerialTimeoutException:



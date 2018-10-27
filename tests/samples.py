# -*- coding: utf-8 -*-


message1 = '\r'.join([
    'MSH|^~\&|MegaReg|XYZHospC|SuperOE|XYZImgCtr|20060529090131-0500||ADT^A01^ADT_A01|01052901|P|2.5',
    'EVN||200605290901||||200605290900',
    'PID|||56782445^^^UAReg^PI||KLEINSAMPLE^BARRY^Q^JR||19620910|M||2028-9^^HL70005^RA99113^^XYZ|260 GOODWIN CREST '
    'DRIVE^^BIRMINGHAM^AL^35209^^M~NICKELL’S PICKLES^10000 W 100TH '
    'AVE^BIRMINGHAM^AL^35200^^O|||||||0105I30001^^^99DEF^AN',
    'PV1||I|W^389^1^UABH^^^^3||||12345^MORGAN^REX^J^^^MD^0010^UAMC^L||67890^GRAINGER^LUCY^X^^^MD^0010^UAMC^L|MED'
    '|||||A0||13579^POTTER^SHERMAN^T^^^MD^0010^UAMC^L|||||||||||||||||||||||||||200605290900',
    'OBX|1|NM|^Body Height||1.80|m^Meter^ISO+|||||F',
    'OBX|2|NM|^Body Weight||79|kg^Kilogram^ISO+|||||F',
    'AL1|1||^ASPIRIN',
    'DG1|1||786.50^CHEST PAIN, UNSPECIFIED^I9|||A'
])

message2 = '\r'.join([
    'MSH|^~&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A04|MSG00001|P|2.4',
    'EVN|A01-|198808181123',
    'PID|||PATID1234^5^M11||JONES^WILLIAM^A^III&Jr||19610615|M-||2106-3|1200 N ELM '
    'STREET^^GREENSBORO^NC^27401-1020|GL|( '
    '919)379-1212|(919)271-3434~(919)277-3114||S||PATID12345001^2^M10|123456789|9-87654^NC',
    'NK1|1|JONES^BARBARA^K|SPO|||||20011105',
    'NK1|1|JONES^MICHAEL^A|FTH',
    'PV1|1|I|2000^2012^01||||004777^LEBAUER^SIDNEY^J.|||SUR||-||1|A0-',
    'AL1|1||^PENICILLIN||PRODUCES HIVES~RASH',
    'AL1|2||^CAT DANDER',
    'DG1|001|I9|1550|MAL NEO LIVER, PRIMARY|19880501103005|F||',
    'PR1|2234|M11|111^CODE151|COMMON PROCEDURES|198809081123',
    'ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^SMITH^ELLEN|199505011201',
    'GT1|1122|1519|BILL^GATES^A',
    'IN1|001|A357|1234|BCMD|||||132987',
    'IN2|ID1551001|SSN12345678',
    'ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^ELLEN|199505011201',
])

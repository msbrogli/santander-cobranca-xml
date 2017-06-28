# encoding: utf-8

import requests
from lxml import etree

basedir = os.path.dirname(__file__)

def render(template, data):
    fullpath = os.path.join(basedir, 'templates/', template)
    template = file(fullpath, 'r').read()
    return template.format(**data)

def get_ticket(data, cert=None):
    url = 'https://ymbdlb.santander.com.br/dl-ticket-services/TicketEndpointService'
    request_xml = render('solicitacao_ticket.xml', data)
    ret = requests.post(url, data=request_xml, cert=cert)
    ret_xml = etree.fromstring(str(ret.text))
    (ticket,) = ret_xml.xpath('//ticket')
    (retCode,) = ret_xml.xpath('//retCode')
    return retCode.text, ticket.text

def incluir_titulo(ticket, estacao, data_nsu, nsu='', teste=False, cert=None):
    url = 'https://ymbcash.santander.com.br/ymbsrv/CobrancaEndpointService'
    data = {
        'ticket': ticket,
        'tipo_ambiente': 'T' if teste else 'P',
        'nsu': 'TST' if teste else nsu,
        'data_nsu': data_nsu,
        'estacao': estacao,
    }
    request_xml = render('inclusao_titulo.xml', data)
    ret = requests.post(url, data=request_xml, cert=cert)
    return ret

def consultar_titulo(ticket, nsu, data_nsu, estacao, teste=False, cert=None):
    url = 'https://ymbcash.santander.com.br/ymbsrv/CobrancaEndpointService'
    data = {
        'data_nsu': data_nsu,
        'nsu': nsu,
        'ticket': ticket,
        'estacao': estacao,
        'tipo_ambiente': 'T' if teste else 'P',
    }
    request_xml = render('consulta_titulo.xml', data)
    ret = requests.post(url, data=request_xml, cert=cert)
    return ret


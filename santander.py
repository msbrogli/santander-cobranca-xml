# encoding: utf-8

import requests
import os
from lxml import etree
from collections import namedtuple

basedir = os.path.dirname(__file__)

GetTicketResponse = namedtuple('TicketResponse', 'return_code ticket response')
IncluirTituloResponse = namedtuple('IncluirTituloResponse', 'situacao descricao response')
ConsultarTituloResponse = namedtuple('ConsultarTituloResponse', 'situacao descricao response')

def xml_prettyprint(txt):
    import xml.dom.minidom
    return xml.dom.minidom.parseString(txt.encode('utf-8')).toprettyxml()

def render(template, data):
    fullpath = os.path.join(basedir, 'templates/', template)
    template = file(fullpath, 'r').read()
    return template.format(**data)

def get_ticket(data, cert=None):
    url = 'https://ymbdlb.santander.com.br/dl-ticket-services/TicketEndpointService'
    request_xml = render('solicitacao_ticket.xml', data)
    ret = requests.post(url, data=request_xml, cert=cert)
    ret_xml = etree.fromstring(ret.text.encode('utf-8'))
    (ticket,) = ret_xml.xpath('//ticket')
    (retCode,) = ret_xml.xpath('//retCode')
    return GetTicketResponse(int(retCode.text), ticket.text, xml_prettyprint(ret.text))

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
    ret_xml = etree.fromstring(ret.text.encode('utf-8'))
    (situacao,) = ret_xml.xpath('//situacao')
    (descricao,) = ret_xml.xpath('//descricaoErro')
    return IncluirTituloResponse(situacao.text, descricao.text, xml_prettyprint(ret.text))

def consultar_titulo(ticket, nsu, data_nsu, estacao, teste=False, cert=None):
    url = 'https://ymbcash.santander.com.br/ymbsrv/CobrancaEndpointService'
    data = {
        'ticket': ticket,
        'tipo_ambiente': 'T' if teste else 'P',
        'nsu': nsu,
        'data_nsu': data_nsu,
        'estacao': estacao,
    }
    request_xml = render('consulta_titulo.xml', data)
    ret = requests.post(url, data=request_xml, cert=cert)
    ret_xml = etree.fromstring(ret.text.encode('utf-8'))
    (situacao,) = ret_xml.xpath('//situacao')
    (descricao,) = ret_xml.xpath('//descricaoErro')
    return ConsultarTituloResponse(situacao.text, descricao.text, xml_prettyprint(ret.text))


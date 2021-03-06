# coding=utf8

# Copyright (C) 2015, Vanessa Soares, Thaiane Braga
#
# This file is part of Radar Parlamentar.
#
# Radar Parlamentar is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Radar Parlamentar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Radar Parlamentar.  If not, see <http://www.gnu.org/licenses/>.# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.staticfiles import finders
from analises.genero import Genero
import os
import datetime
import json
import logging

logger = logging.getLogger("radar")

def index(request):
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))


def origem(request):
    return render_to_response('origem.html', {},
                              context_instance=RequestContext(request))


def ogrupo(request):
    return render_to_response('grupo.html', {},
                              context_instance=RequestContext(request))


def premiacoes(request):
    return render_to_response('premiacoes.html', {},
                              context_instance=RequestContext(request))


def radar_na_midia(request):
    return render_to_response('radar_na_midia.html', {},
                              context_instance=RequestContext(request))


def votoaberto(request):
    return render_to_response('votoaberto.html', {},
                              context_instance=RequestContext(request))


def importadores(request):
    return render_to_response('importadores.html', {},
                              context_instance=RequestContext(request))


def grafico_alternativo(request):
    return render_to_response('grafico_alternativo.html', {},
                              context_instance=RequestContext(request))


def genero(request):
    return render_to_response('genero.html', {},
                              context_instance=RequestContext(request))


def genero_termos_nuvem(request):
  genero = Genero()

  temas_frequencia_mulher = genero.definir_palavras('F')
 # logger.info("Temasdamulher %s" % (temas_frequencia_mulher))
  temas_json_mulher = json.dumps(temas_frequencia_mulher)

  temas_frequencia_homem = genero.definir_palavras('M')
  temas_json_homem = json.dumps(temas_frequencia_homem)

  return render_to_response('genero_tagcloud.html', {'temas_mulher': temas_json_mulher,'temas_homem': temas_json_homem},
                              context_instance=RequestContext(request))

def genero_matriz(request):
    return render_to_response('genero_matriz.html', {},
                              context_instance=RequestContext(request))


def genero_treemap(request):
    return render_to_response('genero_treemap.html', {},
                              context_instance=RequestContext(request))


def genero_historia_legislaturas(request):
    return render_to_response('genero_historia.html', {},
                              context_instance=RequestContext(request))


def genero_perfil_partido(request):
    return render_to_response('genero_perfil_partido.html', {},
                              context_instance=RequestContext(request))


def genero_comparativo_partidos(request):
    return render_to_response('genero_comparativo_partidos.html', {},
                              context_instance=RequestContext(request))


def genero_futuro(request):
    return render_to_response('genero_futuro.html', {},
                              context_instance=RequestContext(request))


def genero_perfil_legis(request):
    return render_to_response('perfil_legis.html', {},
                              context_instance=RequestContext(request))


def dados_utilizados(request):
    dump_file_path = finders.find('db-dump/radar.sql')
    time = os.path.getmtime(dump_file_path)
    dt = datetime.datetime.fromtimestamp(time)
    dt_str = dt.strftime('%d/%m/%Y')
    return render_to_response('dados_utilizados.html', {'dumpdate':dt_str}, 
                              context_instance=RequestContext(request))




#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import *
import time
from fpdf import FPDF
import os

#==== Evidências em .pdf
pdf = FPDF(orientation='P', unit='mm', format='A4')
counter = 1

def InsertEvidence(stepText, textValidation, status):
    pdf.add_page()
    global counter

    #==== Borda na página
    pdf.set_line_width(0.0)
    pdf.line(5.0, 5.0, 205.0, 5.0)  # top one
    pdf.line(5.0, 292.0, 205.0, 292.0)  # bottom one
    pdf.line(5.0, 5.0, 5.0, 292.0)  # left one
    pdf.line(205.0, 5.0, 205.0, 292.0)  # right one

    # ==== Texto
    pdf.set_font('Arial', '', 14)
    pdf.cell(10, 10, str(str(counter) + ") " + stepText))
    pdf.ln(5)

    if (status == "Aprovado"):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(10, 10, "Status: ")

        pdf.set_font('Arial', '', 12)
        pdf.set_text_color(33, 118, 33)
        pdf.cell(10, 10, "     Aprovado")
        pdf.set_text_color(0, 0, 0)
    elif (status == "Reprovado"):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(10, 10, "Status: ")

        pdf.set_font('Arial', '', 12)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(10, 10, "     Reprovado")
        pdf.set_text_color(0, 0, 0)

    pdf.set_font('Arial', 'I', 12)
    pdf.ln(10)
    pdf.cell(10, 10, str(textValidation + ":"))

    # ==== Print
    if os.path.exists("evidences\\screenshot" + str(counter) + ".png"):
        pdf.image("evidences\\screenshot" + str(counter) + ".png", x=10, y=50, w=190)
        os.remove("evidences\\screenshot" + str(counter) + ".png")

    counter += 1
    return


#==== Steps

@given('que acessei o site OrangeHRM')
def step_impl(context):
    global counter
    stepText = "Dado que acessei o site OrangeHRM"
    try:
        context.driver.get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/")

        context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
        textValidation = "Após acessar o site OrangeHRM"
        InsertEvidence(stepText, textValidation, "Aprovado")
    except:
        context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
        textValidation = "Site não acessado"
        InsertEvidence(stepText, textValidation, "Reprovado")
    return

@given('que loguei no site')
def step_impl(context):
    global counter
    stepText = "Dado que loguei no site"
    try:
        context.driver.find_element_by_id("txtUsername").send_keys("opensourcecm")
        context.driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
        context.driver.find_element_by_id("btnLogin").click()

        try:
            context.driver.find_element_by_id("option-menu")
            context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
            textValidation = "Após logar no site"
            InsertEvidence(stepText, textValidation, "Aprovado")
        except:
            context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
            textValidation = "Login não realizado"
            InsertEvidence(stepText, textValidation, "Reprovado")

    except:
        context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
        textValidation = "Login não realizado"
        InsertEvidence(stepText, textValidation, "Reprovado")
    return

@when('eu procuro um funcionário inexistente')
def step_impl(context):
    global counter
    stepText = "Quando eu procuro um funcionário inexistente"
    try:
        #Realizando a busca
        context.driver.switch_to.frame(context.driver.find_element_by_id('rightMenu'))
        context.driver.find_element_by_id("empsearch_employee_name_empName").click
        context.driver.find_element_by_id("empsearch_employee_name_empName").send_keys("Joao")
        time.sleep(2)
        context.driver.find_element_by_id("searchBtn").send_keys("\n")

        #Validação dos resultados
        valorSpan = context.driver.find_element_by_xpath("/html/body/div[1]/span").text
        if (valorSpan == "No Employees Available"):
            context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
            textValidation = 'Após a busca. Mensagem de "Usuário não encontrado".'
            InsertEvidence(stepText, textValidation, "Aprovado")
    except:
        context.driver.save_screenshot("evidences\\screenshot" + str(counter) + ".png")
        textValidation = "Busca não realizada"
        InsertEvidence(stepText, textValidation, "Reprovado")
    return

@then('gero uma evidência')
def step_impl(context):
    #Exportando o .pdf
    if (os.path.exists('evidences/Evidence-' + time.strftime("%H") + "-" + time.strftime("%M") + '.pdf')):
        pdf.output('evidences/Evidence-' + time.strftime("%H") + "-" + time.strftime("%M") + '(2).pdf', 'F')
    else:
        pdf.output('evidences/Evidence-' + time.strftime("%H") + "-" + time.strftime("%M") + '.pdf', 'F')
from django.test import TestCase
from django.urls import reverse

class TestPaginaInicial(TestCase):
    def test_redirecionamento_para_pagina_inicial(self):
        response = self.client.get(reverse('pagina_inicial')) 

        self.assertEqual(response.status_code, 200)  # Verifica se a resposta tem status 200 (OK)
        self.assertTemplateUsed(response, 'pagina_inicial.html')  # Verifica se o modelo correto foi usado

    def test_redirecionamento_para_pagina_inicial_com_url(self):
        url = '/template/'  # Substitua pelo URL real da sua página inicial
        response = self.client.get(url)

        self.assertRedirects(response, reverse('pagina_inicial'))  # Verifica se há um redirecionamento para a página inicial

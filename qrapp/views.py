from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import qrcode


from agents.utils import chiffrement, dechiffrement
from agents.models import Agent
# Create your views here.


def generate_qr(request, id_agent):
    """ Générer le code QR """
    # Recuperer l'agent
    agent = get_object_or_404(Agent, pk=id_agent)

    # Recuperer les informations
    name = agent.name
    firstname = agent.firstname

    # Concatener les donnees recuperees en les stockant en majuscule
    chaine = name.upper() + ' ' + firstname.upper()

    print(f'chaine : {chaine}')
    
    # Chiffrement des donnees
    code = chiffrement(chaine)

    # Récupérer le code de l'agent
    data = code

    # Générer le code QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
  

    # Générez une image du code QR
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Créez une réponse HTTP pour télécharger l'image
    response = HttpResponse(content_type="image/png")
    qr_image.save(response, "PNG")
    response['Content-Disposition'] = f'attachment; filename="{agent.name}qr_code.png"'

    return response


def dechiffrer(request):
    """ Dechiffrer le code provenant du QR """
    # Recuperer tous les agent
    agents = Agent.objects.all()

    if request.method == 'POST':
        """ Verifier si la methode est POST """

        # Recuperer la donnee du formulaire
        code  = request.POST.get('code')

        # Dechiffrer le code
        decode = dechiffrement(code)

        # Rechercher l'agent
        for agent in agents:
            if agent.name + ' ' + agent.firstname == decode:
                return redirect('agent', id=agent.id)

    return render(request, 'qr_generator/dechiffre.html')


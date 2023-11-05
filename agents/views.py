from django.shortcuts import render, get_object_or_404, redirect
from .forms import AgentForm
from .models import Agent

# Create your views here.

def addAgent(request):
    """ Ajouter un agent """

    # formulaire avec fichier image
    form = AgentForm()
    ajout = ""
    if request.method == 'POST':
        """ Verifier si la methode est POST """
        form = AgentForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            """ Verifier si le formulaire est valide """

            # Enregistrer le formulaire sans executer le commit des donnees
            form.save()
            
            ajout = "ok"
            return render(request, 'agent/add_agent.html', {'form': form, 'ajout': ajout})
        
    return render(request, 'agent/add_agent.html', {'form': form, 'ajout': ajout})


def agentView(request, id):
    """ Afficher les informations d'un agent """
    agent = get_object_or_404(Agent, pk=id)
    if request.method == 'POST':
        """ Verifier si la methode est POST  """
        # Rediriger vers la vu de l'agent
        return redirect('generate_qr', id_agent=agent.id)
    return render(request, 'agent/agent.html', {'agent': agent})


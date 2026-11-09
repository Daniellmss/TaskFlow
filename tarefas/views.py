from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.contrib import messages

# Create your views here.
def paginaInicial(request):
    mensagem = "Gerencie suas tarefas com facilidade!"
    tarefas = Tarefa.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome") or ""
        descricao = request.POST.get("descricao") or ""
        descricao = descricao.strip()
        try: 
            prioridade = int(request.POST.get("prioridade"))
            if not 1 <= prioridade <= 3:
                messages.error(request, 'Valor invalido!')
                return redirect('pagina_inicial')
        except ValueError: 
            messages.error(request, 'Valor invalido!')
            return redirect('pagina_inicial')
        if not nome.strip():
            messages.error(request, 'Nome inválido!')
        else: 
            nome = nome.strip()
            Tarefa.objects.create(
                nome= nome, 
                descricao = descricao, 
                prioridade = prioridade
            )
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('pagina_inicial')                         
    return render(request, 'tarefas/index.html', {"mensagem": mensagem,"tarefas": tarefas})

def concluirTarefa(request, id):
    if request.method == "POST":
        tarefa = get_object_or_404(Tarefa, id=id)
        if tarefa.concluida:
            messages.success(request, 'Tarefa foi reaberta!')
        else:
            messages.success(request, 'Tarefa foi concluida!')
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        return redirect('pagina_inicial')

def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == "POST":
        nome = request.POST.get("nome") or ""
        descricao = request.POST.get("descricao") or ""
        nome = nome.strip()
        descricao = descricao.strip()
        try:
            prioridade = int(request.POST.get("prioridade"))
            if not 1<= prioridade <= 3:
                messages.error(request, "Valor invalido!")
                return redirect('pagina_inicial')
        except ValueError:
            messages.error(request, "Valor invalido")
            return redirect('pagina_inicial')
        if not nome:
            messages.error(request, "nome invalido!")
            return redirect('pagina_inicial')
        tarefa.nome = nome
        tarefa.descricao = descricao
        tarefa.prioridade = prioridade
        tarefa.save()
        messages.success(request, "Tarefa salva!")
        return redirect('pagina_inicial')
    return render(request, 'tarefas/editar.html', {"tarefa": tarefa})

def excluirTarefa(request, id):
    if request.method == "POST":
        tarefa = get_object_or_404(Tarefa, id=id)
        tarefa.delete()
        messages.success(request, "Tarefa apagada com sucesso!")
        return redirect('pagina_inicial')

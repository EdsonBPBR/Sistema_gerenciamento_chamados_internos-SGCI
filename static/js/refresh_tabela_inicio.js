function atualizarChamados() {
    fetch('/sgci/admin/api/chamados_abertos')
        .then(response => response.json())
        .then(data => {
            let html = "";
            data.chamados.forEach(registro => {
                const prioridade = registro['prioridade'].toLowerCase();
                let badgeClass = 'secondary';
                
                if (prioridade === 'alta') {
                    badgeClass = 'danger';
                } else if (prioridade === 'media') {
                    badgeClass = 'warning';
                } else if (prioridade === 'baixa') {
                    badgeClass = 'secondary';
                }
                
                const prioridadeTexto = registro['prioridade'].charAt(0).toUpperCase() + 
                                        registro['prioridade'].slice(1);
                
                html += `
                <tr>
                    <th scope="row">${registro['nome_solicitante']}</th>
                    <td>${registro['tipo_servico'].charAt(0).toUpperCase() + registro['tipo_servico'].slice(1)}</td>
                    <td>${registro['setor'].charAt(0).toUpperCase() + registro['setor'].slice(1)}</td>
                    <td>
                        <span class="badge text-bg-${badgeClass}">
                            ${prioridadeTexto}
                        </span>
                    </td>
                    <td>${registro['data']} ${registro['horario']}</td>
                </tr>`;
            });
            document.getElementById("tabela-abertos").innerHTML = html;
        });
}

atualizarChamados();              
setInterval(atualizarChamados, 20000);
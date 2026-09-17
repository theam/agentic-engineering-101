# Security policy

*[Versión en español más abajo](#política-de-seguridad).*

This repository is mostly prose, but its labs ask you to run coding agents with
permissions on your machine. A lab step that could leak secrets, run
destructive commands or expose readers to prompt injection is a security issue
for us.

## Reporting

Report privately via
[GitHub's private vulnerability reporting](https://github.com/theam/agentic-engineering-101/security/advisories/new)
("Report a vulnerability" in the Security tab). Please don't open a public
issue for:

- lab instructions or prompts that could cause data loss, leak credentials or
  escalate an agent's permissions,
- vulnerabilities in the practice project or the scripts in this repository,
- links that now point to malicious content.

We aim to acknowledge reports within five working days. Once a fix is merged, we
will credit you if you want.

Typos, broken links and outdated advice without a security impact are regular
issues. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Safe defaults in this guide

- Labs never require production credentials. Use a practice repository or a
  throwaway branch.
- Anything that bypasses an agent's permission prompts should only run inside an
  isolated environment (container, VM or sandbox) with no secrets. Module 03
  explains why.

---

## Política de seguridad

Este repositorio es sobre todo texto, pero sus laboratorios te piden ejecutar
agentes de programación con permisos en tu máquina. Para nosotros es un problema
de seguridad cualquier paso de un laboratorio que pueda filtrar secretos,
ejecutar comandos destructivos o exponer a quien lo lee a una inyección de
prompts.

### Cómo reportar

Repórtalo en privado mediante el
[reporte privado de vulnerabilidades de GitHub](https://github.com/theam/agentic-engineering-101/security/advisories/new)
("Report a vulnerability" en la pestaña Security). Por favor, no abras una issue
pública para:

- instrucciones o prompts de los laboratorios que puedan causar pérdida de
  datos, filtrar credenciales o ampliar los permisos de un agente,
- vulnerabilidades en el proyecto de prácticas o en los scripts del repositorio,
- enlaces que ahora apunten a contenido malicioso.

Intentamos confirmar la recepción en un máximo de cinco días laborables. Cuando
el arreglo esté mergeado, te daremos crédito si quieres.

Las erratas, los enlaces rotos y los consejos desactualizados sin impacto en la
seguridad son issues normales. Consulta [CONTRIBUTING.es.md](CONTRIBUTING.es.md).

### Valores seguros por defecto en esta guía

- Los laboratorios nunca requieren credenciales de producción. Usa un
  repositorio de prácticas o una rama desechable.
- Cualquier cosa que se salte las confirmaciones de permisos de un agente solo
  debe ejecutarse en un entorno aislado (contenedor, máquina virtual o sandbox)
  sin secretos. El módulo 03 explica por qué.

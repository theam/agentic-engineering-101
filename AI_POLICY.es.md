# Política de IA

[Read in English](AI_POLICY.md)

Esta guía enseña a construir software con agentes de IA, así que prohibir las
contribuciones hechas con IA no tendría sentido. Pero revisar una contribución
cuesta tiempo a quien mantiene el proyecto, la haya escrito quien la haya
escrito. Estas reglas mantienen ese coste en un nivel razonable.

Están adaptadas de las políticas de [LLVM](https://llvm.org/docs/AIToolPolicy.html),
[Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md),
el [kernel de Linux](https://docs.kernel.org/process/coding-assistants.html) y
[Fedora](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/).

## Las reglas

1. **Siempre hay una persona responsable.** Cada issue, pull request y
   comentario lo envía una persona que responde por él. Los agentes preparan el
   trabajo y las personas lo envían. No aceptamos pull requests abiertos de
   forma autónoma por agentes sin que una persona los haya revisado antes.
2. **Declara la asistencia.** Rellena la sección "AI assistance" de la plantilla
   del pull request: qué herramienta y modelo usaste y qué hicieron (redactar,
   traducir, revisar enlaces, escribir código…). Añade este trailer a los
   commits en los que haya contribuido un agente:

   ```text
   Assisted-by: Claude Code (<modelo>)
   ```

   Un agente nunca debe añadir `Signed-off-by` ni ninguna otra declaración en
   nombre de una persona.
3. **Entiende y verifica lo que envías.** Lee el diff entero. Ejecuta
   `python3 scripts/check_content.py`. Si has cambiado un laboratorio, hazlo.
   Si has cambiado el proyecto de prácticas, ejecuta sus tests. Si una
   afirmación o una cita viene de un agente, abre la fuente y comprueba que de
   verdad dice eso.
4. **Nada de contribuciones extractivas.** Una contribución debe aportar más de
   lo que cuesta revisarla. Cerraremos los cambios grandes, no solicitados y
   poco verificados (un módulo entero generado de una vez, reescrituras
   masivas, issues en bloque) con un enlace a esta política. Propón los cambios
   grandes primero en una issue.
5. **Un agente puede hacer el borrador de una traducción, pero la revisa una
   persona.** Alguien con dominio del idioma revisa cada traducción hecha por
   un agente antes de mergearla. Usa la etiqueta `translation-review` si tú no
   puedes hacer esa revisión.
6. **Deja fuera el material confidencial.** No pegues código privado,
   información de clientes ni credenciales en los prompts que uses para
   escribir en este repositorio, y mucho menos en el propio repositorio.
7. **Quien mantiene el proyecto también usa IA, con las mismas reglas.**

## Por qué "declarar" y no "prohibir"

Declarar la asistencia ayuda a quien revisa a poner la atención donde hace
falta. Además, deja un registro público de cómo se usan los agentes para
escribir material formativo, que es en sí mismo parte de lo que enseña esta
guía. Usar un agente nunca jugará en tu contra. Saltarte la declaración o la
verificación, sí.

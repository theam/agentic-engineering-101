# Cómo contribuir

[Read in English](CONTRIBUTING.md)

Gracias por ayudar. Esta guía existe porque la práctica del agentic engineering
todavía se está definiendo y ningún equipo ha visto lo suficiente por sí solo.
Tu experiencia, incluido lo que no te funcionó, mejora la guía para todos los
que la lean después.

## Formas de contribuir

| Si quieres… | Haz esto |
|---|---|
| Corregir una errata, un enlace roto o un comando incorrecto | Abre un pull request directamente |
| Avisar de algo incorrecto o confuso | [Abre una issue de "content error"](https://github.com/theam/agentic-engineering-101/issues/new?template=content-error.yml) |
| Compartir cómo trabajas tú o tu equipo | [Abre una issue de "share your practice"](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml). Es la contribución más valiosa que recibimos |
| Avisar de que una herramienta ha cambiado (un flag renombrado, una función que ya no existe) | [Abre una issue de "tool drift"](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) |
| Proponer una lección, un laboratorio o una sección nuevos | [Abre una issue de "lesson proposal"](https://github.com/theam/agentic-engineering-101/issues/new?template=lesson-proposal.yml) y coméntalo antes de escribir |
| Mejorar la redacción en español (o en inglés) | [Abre una issue de "translation"](https://github.com/theam/agentic-engineering-101/issues/new?template=translation.yml) o un pull request |
| Impartir un workshop con este material | Adelante (CC BY 4.0). Después cuéntanos qué funcionó en una issue de "share your practice" |

## Cómo entra un cambio

1. **Arreglos pequeños:** abre un pull request.
2. **Cualquier cosa más grande** (una sección nueva, un cambio de recomendación,
   un laboratorio nuevo): abre antes una issue para acordar el enfoque antes de
   escribir en dos idiomas.
3. Crea una rama, haz el cambio en **inglés y español** y ejecuta las
   comprobaciones de abajo.
4. Abre el pull request con la plantilla. Rellena la sección **AI assistance**
   aunque la respuesta sea "ninguna".
5. Alguien del equipo de mantenimiento lo revisa. Intentamos responder en menos
   de una semana. Los cambios de contenido necesitan una aprobación. Los cambios
   de recomendación o de estructura necesitan la conversación del paso 2.

### Los dos idiomas en el mismo pull request

El inglés es la fuente de verdad, pero la versión en español no es secundaria.
Actualiza ambas en el mismo pull request. Si no dominas uno de los dos idiomas:

- escribe el que domines,
- deja que un agente haga un borrador del otro (y decláralo), y
- añade la etiqueta `translation-review` para que alguien con dominio del idioma
  lo revise antes de mergear.

Los detalles están en [docs/authoring.es.md](docs/authoring.es.md#traducción).

### Comprobaciones locales

```bash
python3 scripts/check_content.py                 # estructura, paridad de idiomas, enlaces relativos
npx markdownlint-cli2 "**/*.md"                  # estilo Markdown (opcional en local; lo ejecuta la CI)
cd practice/shelf && python -m unittest          # solo si has cambiado el proyecto de prácticas
```

La CI ejecuta las mismas comprobaciones y además valida los enlaces externos.

## Estilo

Lee [docs/authoring.es.md](docs/authoring.es.md) antes de escribir. En resumen:

- Primero lo concreto, frases cortas, explica el *porqué* y señala claramente
  los enfoques equivocados.
- La práctica de la empresa se escribe como "En The Agile Monkeys…". Tu propia
  práctica puede ir como "un equipo que conocemos…" o con tu nombre, si quieres
  el crédito.
- Cita las voces públicas con nombre y enlace. Las citas deben ser literales y
  de 25 palabras como máximo.
- Mantén los matices. Cuando los expertos no coinciden, muestra ambas posturas.
- Nunca incluyas información confidencial: nombres de clientes, URLs internas,
  credenciales, nada que no publicarías en un blog público.
- No hagas referencia a reuniones o sesiones internas de The Agile Monkeys, ni
  a qué persona del equipo compartió una práctica, ni en el contenido ni en
  mensajes de commit, pull requests o nombres de rama. Todo es público. Tu
  propia práctica puede seguir llevando tu nombre, como se indica arriba.

## Contribuciones asistidas por IA

Son bienvenidas, bajo nuestra [política de IA](AI_POLICY.es.md). En resumen: una
persona es responsable de cada contribución, la asistencia de IA se declara y
todo se verifica antes de enviarlo. Si eres un agente, lee [AGENTS.md](AGENTS.md).

## Mantenimiento

The Agile Monkeys mantiene este proyecto. Personas que lo mantienen ahora mismo:

- [@javiertoledo](https://github.com/javiertoledo)

Quien mantiene el proyecto revisa pull requests, clasifica issues y decide los
cambios de estructura y de recomendaciones. Decidimos conversando en la issue o
en el pull request. Si no hay consenso, decide el equipo de mantenimiento.
Abriremos este rol a quienes contribuyan con regularidad a medida que crezca la
comunidad.

Para reportar en privado un problema relacionado con el Código de Conducta,
escribe a alguien del equipo de mantenimiento a través de su perfil de GitHub.
Si el problema afecta a esa persona, contacta con otra.

## Reconocimiento

Cada contribución mergeada queda acreditada en el historial de git. Si quieres,
quien comparta una práctica que acabe en una lección aparece en la sección
"Para profundizar" de esa lección.

## Licencia de las contribuciones

Al contribuir aceptas que tus aportaciones se publiquen con las licencias del
repositorio: [CC BY 4.0](LICENSE) para el contenido de la guía y
[MIT](LICENSE-CODE) para el código. Es la regla "inbound = outbound" de los
[Términos de Servicio de GitHub](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#6-contributions-under-repository-license).
No hay que firmar ningún CLA.

Quien participa acepta nuestro [Código de Conducta](CODE_OF_CONDUCT.es.md).

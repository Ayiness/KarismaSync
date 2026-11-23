# Spec Delta — asistencia-convocatoria

## Purpose

Permitir que cada músico convocado responda la convocatoria de un evento de ensayo (confirmar o no asistir con motivo, y cambiar su respuesta mientras el evento esté vigente) y que el Líder de Alabanza y los convocados vean el estado de las respuestas.

## ADDED Requirements

### Requirement: Confirmar la asistencia con los instrumentos asignados

El sistema DEBE permitir que un músico convocado confirme su asistencia a un evento vigente y DEBE registrarla como Confirmada con los instrumentos que el Líder de Alabanza le asignó en la convocatoria.

#### Scenario: El integrante confirma su asistencia y ve los instrumentos asignados

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Pedro fue convocado con guitarra eléctrica y voz
- **WHEN** Pedro confirma que asistirá al ensayo
- **THEN** Pedro queda registrado como asistente del ensayo
- **AND** guitarra eléctrica y voz quedan registrados como sus instrumentos para ese ensayo
- **AND** su respuesta queda considerada en la evaluación del quórum y de los roles requeridos

### Requirement: Informar la no asistencia con un motivo obligatorio

El sistema DEBE permitir que un músico convocado informe que no asistirá a un evento vigente indicando un motivo de hasta 200 caracteres, y NO DEBE registrar la respuesta si falta el motivo.

#### Scenario: El integrante informa que no asistirá

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Pedro fue convocado con guitarra eléctrica
- **WHEN** Pedro informa que no asistirá al ensayo porque «tengo turno en el trabajo»
- **THEN** Pedro queda registrado como no asistente del ensayo con el motivo «tengo turno en el trabajo»
- **AND** no se registran instrumentos a su nombre para ese ensayo

#### Scenario: El integrante intenta informar que no asistirá sin indicar el motivo

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Pedro fue convocado con guitarra eléctrica
- **WHEN** Pedro informa que no asistirá al ensayo sin escribir un motivo
- **THEN** la respuesta de Pedro no queda registrada y su asistencia sigue pendiente
- **AND** Pedro es informado de que debe indicar el motivo por el que no asistirá

### Requirement: Cambiar la respuesta mientras el evento esté vigente

El sistema DEBE permitir que el músico convocado cambie su respuesta mientras el evento esté vigente: de Confirmada a No asiste indicando el motivo, o de No asiste a Confirmada borrando el motivo anterior.

#### Scenario: El integrante cambia su respuesta de confirmada a no asiste

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Pedro confirmó su asistencia
- **WHEN** Pedro cambia su respuesta e informa que no asistirá porque «me enfermé»
- **THEN** Pedro queda registrado como no asistente del ensayo con el motivo «me enfermé»

#### Scenario: El integrante cambia su respuesta de no asiste a confirmada

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Pedro informó que no asistirá porque «tengo turno en el trabajo»
- **WHEN** Pedro cambia su respuesta y confirma que asistirá
- **THEN** Pedro queda registrado como asistente del ensayo
- **AND** el motivo «tengo turno en el trabajo» ya no queda registrado

### Requirement: Mantener los instrumentos definidos por el líder

El sistema NO DEBE permitir que el integrante cambie los instrumentos de su convocatoria y DEBE informarle que solo el Líder de Alabanza puede asignarlos.

#### Scenario: El integrante intenta cambiar los instrumentos de su convocatoria

- **GIVEN** Pedro fue convocado con guitarra eléctrica y voz
- **WHEN** Pedro intenta reemplazar guitarra eléctrica por guitarra acústica
- **THEN** los instrumentos de su convocatoria no cambian
- **AND** Pedro es informado de que solo el Líder de Alabanza puede asignar los instrumentos

### Requirement: Responder solo convocatorias vigentes

El sistema NO DEBE registrar respuestas a un evento que no está vigente y DEBE informar que la convocatoria ya no está disponible.

#### Scenario: El integrante intenta confirmar después de que el evento fue cancelado

- **GIVEN** el evento de ensayo del sábado 14 de noviembre fue cancelado
- **WHEN** Pedro intenta confirmar que asistirá
- **THEN** la asistencia de Pedro no queda registrada
- **AND** Pedro es informado de que la convocatoria ya no está disponible

### Requirement: Responder solo si fue convocado

El sistema DEBE permitir que un integrante no convocado vea el evento, pero NO DEBE mostrarle la opción de responder ni las respuestas de los convocados, ni registrar una respuesta suya.

#### Scenario: Un integrante no convocado abre el evento

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Sofía no fue convocada a ese evento
- **WHEN** Sofía abre el evento
- **THEN** Sofía ve la fecha del ensayo
- **AND** Sofía no ve la opción de responder ni las respuestas de los convocados

#### Scenario: Un integrante no convocado intenta confirmar su asistencia

- **GIVEN** el evento de ensayo del sábado 14 de noviembre está vigente
- **AND** Sofía no fue convocada a ese evento
- **WHEN** Sofía intenta confirmar que asistirá
- **THEN** la asistencia de Sofía no queda registrada
- **AND** Sofía es informada de que no fue convocada a este evento

### Requirement: Mostrar el estado de las respuestas de los convocados

El sistema DEBE mostrar al Líder de Alabanza y a los músicos convocados, en el detalle del evento, a cada convocado con sus instrumentos y el estado de su respuesta. El motivo de inasistencia es privado: el sistema DEBE mostrarlo solo al Líder de Alabanza y al propio integrante.

#### Scenario: El líder revisa el estado de las respuestas de los convocados

- **GIVEN** Marta creó el evento del sábado 14 de noviembre convocando a Pedro, Ana y Luis
- **AND** Pedro confirmó su asistencia
- **AND** Ana informó que no asistirá porque «tengo turno en el trabajo»
- **AND** Luis todavía no responde
- **WHEN** Marta abre el detalle del evento
- **THEN** ve a Pedro con su instrumento y el estado Confirmada
- **AND** ve a Ana con su instrumento, el estado No asiste y el motivo «tengo turno en el trabajo»
- **AND** ve a Luis con su instrumento y el estado Pendiente

#### Scenario: Un músico convocado revisa las respuestas sin ver los motivos de los demás

- **GIVEN** Marta creó el evento del sábado 14 de noviembre convocando a Pedro, Ana y Luis
- **AND** Ana informó que no asistirá porque «tengo turno en el trabajo»
- **WHEN** Luis abre el detalle del evento
- **THEN** ve a Ana con su instrumento y el estado No asiste
- **AND** no ve el motivo de Ana

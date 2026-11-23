# eventos-ensayo Specification

## Purpose
Gestionar la creación y convocatoria de los eventos de ensayo de la banda, asegurando que solo el Líder de Alabanza los cree con fecha, un quórum indicado que no supere a los convocados y los músicos convocados con sus instrumentos, y que solo los convocados reciban el aviso.

## Requirements

### Requirement: Restringir la creación de eventos al Líder de Alabanza

El sistema DEBE rechazar la creación de un evento cuando el usuario no tiene el rol de Líder de Alabanza, sin registrar el evento ni enviar convocatorias, e informarle que solo ese rol puede crear eventos de ensayo.

#### Scenario: Un integrante sin rol de líder intenta crear un evento de ensayo

- **GIVEN** Pedro es integrante de la banda y no tiene el rol de Líder de Alabanza
- **WHEN** Pedro intenta crear un evento de ensayo para el sábado 14 de noviembre
- **THEN** el evento de ensayo no queda registrado
- **AND** ningún integrante recibe una convocatoria
- **AND** Pedro es informado de que solo el Líder de Alabanza puede crear eventos de ensayo

### Requirement: Exigir el quórum del ensayo

El sistema DEBE rechazar la creación de un evento cuando no se indica el quórum o cuando el quórum supera la cantidad de músicos convocados, sin registrar el evento ni enviar convocatorias, e informar al líder el motivo.

#### Scenario: El líder intenta crear un evento de ensayo sin quórum

- **GIVEN** Marta tiene el rol de Líder de Alabanza y Pedro y Ana están convocados con sus instrumentos principales
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin indicar el quórum
- **THEN** el evento de ensayo no queda registrado
- **AND** ningún integrante recibe una convocatoria
- **AND** Marta es informada de que debe indicar el quórum requerido

#### Scenario: El líder intenta crear un evento con un quórum mayor que los músicos convocados

- **GIVEN** Marta tiene el rol de Líder de Alabanza y Marta, Pedro, Ana y Luis están convocados con sus instrumentos principales
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre con un quórum de 5 integrantes
- **THEN** el evento de ensayo no queda registrado
- **AND** ningún integrante recibe una convocatoria
- **AND** Marta es informada de que el quórum no puede superar la cantidad de músicos convocados

### Requirement: Registrar un evento de ensayo vigente y convocar a los músicos seleccionados

El sistema DEBE mostrar a todos los integrantes de la banda con su instrumento principal preseleccionado, permitir que el Líder de Alabanza elija qué músicos convocar y con qué instrumentos, registrar el evento como Vigente con la fecha, el quórum y los roles que resultan de esos instrumentos, y enviar la convocatoria solo a los músicos convocados.

#### Scenario: La lista de convocados muestra a todos los músicos con su instrumento principal

- **GIVEN** Marta tiene el rol de Líder de Alabanza y la banda tiene 6 integrantes, cada uno con su instrumento principal
- **WHEN** Marta abre el formulario de creación de un evento de ensayo
- **THEN** la lista muestra a los 6 integrantes convocados con su instrumento principal preseleccionado
- **AND** el campo de quórum aparece vacío para que Marta indique el quórum requerido

#### Scenario: El líder crea un evento convocando a toda la banda

- **GIVEN** Marta tiene el rol de Líder de Alabanza y la banda tiene 6 integrantes, cada uno con su instrumento principal
- **WHEN** Marta crea un evento de ensayo para el sábado 14 de noviembre con un quórum de 6 integrantes y los 6 músicos convocados con sus instrumentos principales
- **THEN** el evento de ensayo queda registrado como vigente con la fecha, el quórum y los roles que resultan de esos instrumentos
- **AND** los 6 integrantes de la banda reciben la convocatoria del evento

#### Scenario: El líder convoca solo a los músicos que necesita

- **GIVEN** Marta tiene el rol de Líder de Alabanza y la lista de convocados muestra a los 6 integrantes con su instrumento principal
- **WHEN** Marta quita a Sofía y a Diego de la convocatoria del sábado 14 de noviembre y crea el evento con un quórum de 4 integrantes y los 4 músicos restantes
- **THEN** el evento de ensayo queda registrado como vigente con los roles que resultan de los instrumentos de los 4 convocados
- **AND** los 4 músicos convocados reciben la convocatoria del evento
- **AND** Sofía y Diego no reciben la convocatoria

#### Scenario: El líder cambia o suma instrumentos a un músico convocado

- **GIVEN** Marta tiene el rol de Líder de Alabanza y Pedro está convocado con guitarra eléctrica como su instrumento principal
- **WHEN** Marta le asigna a Pedro guitarra acústica y voz para el ensayo del sábado 14 de noviembre
- **THEN** guitarra acústica y voz quedan registrados como los instrumentos de Pedro en ese evento
- **AND** guitarra eléctrica no queda requerida por Pedro en ese evento

### Requirement: Exigir músicos convocados con instrumentos

El sistema DEBE rechazar la creación de un evento sin músicos convocados o con algún convocado sin instrumentos, sin registrar el evento, e informar al líder.

#### Scenario: El líder intenta crear un evento de ensayo sin músicos convocados

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin ningún músico convocado
- **THEN** el evento de ensayo no queda registrado
- **AND** Marta es informada de que debe convocar al menos un músico

#### Scenario: El líder intenta crear un evento con un músico convocado sin instrumentos

- **GIVEN** Marta tiene el rol de Líder de Alabanza y Ana está convocada sin ningún instrumento asignado
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre
- **THEN** el evento de ensayo no queda registrado
- **AND** Marta es informada de que cada músico convocado debe tener al menos un instrumento

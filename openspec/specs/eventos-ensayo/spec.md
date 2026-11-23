# eventos-ensayo Specification

## Purpose
Gestionar la creación y convocatoria de los eventos de ensayo de la banda, asegurando que solo el Líder de Alabanza los cree con fecha, quórum y roles requeridos, y que todos los integrantes reciban el aviso.

## Requirements

### Requirement: Registrar un evento de ensayo vigente y convocar a la banda

El sistema DEBE registrar el evento con la fecha, el quórum y al menos un rol requerido, dejarlo en estado Vigente y emitir una convocatoria a todos los integrantes de la banda.

#### Scenario: El líder crea un evento de ensayo y la banda es convocada

- **GIVEN** Marta tiene el rol de Líder de Alabanza y la banda tiene 6 integrantes
- **WHEN** Marta crea un evento de ensayo para el sábado 14 de noviembre con un quórum de 4 integrantes y los roles requeridos batería, bajo, guitarra y voz
- **THEN** el evento de ensayo queda registrado como vigente con la fecha, el quórum y los roles requeridos indicados
- **AND** los 6 integrantes de la banda reciben la convocatoria del evento

### Requirement: Restringir la creación de eventos al Líder de Alabanza

El sistema DEBE rechazar la creación de un evento cuando el usuario no tiene el rol de Líder de Alabanza, sin registrar el evento ni enviar convocatorias, e informarle que solo ese rol puede crear eventos de ensayo.

#### Scenario: Un integrante sin rol de líder intenta crear un evento de ensayo

- **GIVEN** Pedro es integrante de la banda y no tiene el rol de Líder de Alabanza
- **WHEN** Pedro intenta crear un evento de ensayo para el sábado 14 de noviembre
- **THEN** el evento de ensayo no queda registrado
- **AND** ningún integrante recibe una convocatoria
- **AND** Pedro es informado de que solo el Líder de Alabanza puede crear eventos de ensayo

### Requirement: Exigir al menos un rol requerido

El sistema DEBE rechazar la creación de un evento cuando no se indica ningún rol requerido, sin registrar el evento, e informar al líder que debe indicar al menos un rol.

#### Scenario: El líder intenta crear un evento de ensayo sin roles requeridos

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin indicar roles requeridos
- **THEN** el evento de ensayo no queda registrado
- **AND** Marta es informada de que debe indicar al menos un rol requerido

### Requirement: Exigir el quórum del ensayo

El sistema DEBE rechazar la creación de un evento cuando no se indica el quórum, sin registrar el evento, e informar al líder que debe indicar el quórum requerido.

#### Scenario: El líder intenta crear un evento de ensayo sin quórum

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta intenta crear un evento de ensayo para el sábado 14 de noviembre sin indicar el quórum
- **THEN** el evento de ensayo no queda registrado
- **AND** Marta es informada de que debe indicar el quórum requerido

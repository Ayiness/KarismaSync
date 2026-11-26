# evento-masivo Specification

## Purpose
Permitir que el Líder de Alabanza cree eventos masivos y que el Representante de músicos de la banda los apruebe o rechace (con justificación) antes de que se publiquen a los convocados (HU-08, HU-09, CU-07, DSS-01, DSS-07, EST-01).

## Requirements

### Requirement: Elegir el tipo de evento al crearlo

El sistema DEBE permitir que el Líder de Alabanza elija el tipo de evento, Ensayo (por defecto) o Evento masivo, y DEBE aplicar al evento masivo las mismas validaciones de HU-01 y el repertorio opcional de HU-07.

#### Scenario: El formulario propone el tipo Ensayo por defecto

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta abre el formulario de creación de un evento
- **THEN** el tipo de evento aparece seleccionado como Ensayo
- **AND** Marta puede cambiarlo a Evento masivo

#### Scenario: El evento masivo valida los mismos datos que un ensayo

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta intenta crear un evento masivo sin quórum
- **THEN** el evento no se crea
- **AND** el sistema informa que debe indicar el quórum

### Requirement: El evento masivo queda pendiente de aprobación

El sistema DEBE registrar el evento masivo como Pendiente de aprobación, NO DEBE publicarlo ni notificar a los convocados, y DEBE solicitar la revisión al Representante de músicos de la banda. Si la banda no tiene representante, NO DEBE crear el evento.

#### Scenario: El líder crea un evento masivo que queda pendiente de aprobación

- **GIVEN** Marta tiene el rol de Líder de Alabanza y Andrés es el Representante de músicos
- **WHEN** Marta crea un evento masivo con datos válidos
- **THEN** el evento queda pendiente de aprobación
- **AND** los músicos convocados no reciben la convocatoria ni pueden responderla
- **AND** Andrés recibe la solicitud de revisión del evento

#### Scenario: El líder crea un ensayo y no pasa por revisión

- **WHEN** Marta crea un evento de tipo Ensayo con datos válidos
- **THEN** el evento queda vigente y los convocados reciben la convocatoria

#### Scenario: Banda sin representante

- **GIVEN** la banda no tiene un Representante de músicos
- **WHEN** Marta intenta crear un evento masivo
- **THEN** el evento no se crea y el sistema informa que la banda necesita un Representante de músicos

### Requirement: Revisar la convocatoria del evento masivo

El sistema DEBE permitir que solo el Representante de músicos de la banda vea los eventos masivos pendientes y los apruebe o rechace. Al aprobar, el evento DEBE quedar Vigente, emitir las convocatorias (asistencia Pendiente) y notificar a los convocados y al líder. Al rechazar, DEBE exigir una justificación de hasta 200 caracteres, dejar el evento Rechazado, no notificar a los convocados e informar la justificación al líder. Un evento ya revisado o de tipo Ensayo NO DEBE revisarse.

#### Scenario: El representante aprueba un evento masivo

- **GIVEN** el evento masivo del sábado 12 de diciembre está pendiente de aprobación
- **WHEN** Andrés aprueba la convocatoria
- **THEN** el evento queda vigente y los convocados reciben la convocatoria con su asistencia pendiente
- **AND** Marta recibe el aviso de que el evento fue aprobado

#### Scenario: El representante rechaza con justificación

- **WHEN** Andrés rechaza la convocatoria con la justificación «Coincide con el concierto regional»
- **THEN** el evento queda rechazado, los convocados no reciben la convocatoria y Marta recibe la justificación

#### Scenario: Rechazo sin justificación

- **WHEN** Andrés rechaza la convocatoria sin escribir una justificación
- **THEN** el rechazo no se registra y el evento sigue pendiente de aprobación

#### Scenario: Evento ya aprobado

- **GIVEN** el evento masivo ya fue aprobado
- **WHEN** Andrés intenta rechazarlo
- **THEN** el sistema informa que el evento ya fue revisado y el evento sigue vigente

#### Scenario: Permisos

- **WHEN** Andrés intenta crear un evento, o Marta intenta aprobar su propio evento masivo
- **THEN** el sistema rechaza la solicitud por falta de permisos

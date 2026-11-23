# repertorio-opcional Specification

## Purpose
Permitir que el Líder de Alabanza incluya, de forma opcional, canciones del catálogo de la banda al crear un evento, y que el repertorio quede registrado y visible en el detalle del evento.

## Requirements

### Requirement: Ofrecer un repertorio opcional activado por defecto

El sistema DEBE mostrar el bloque de repertorio activado por defecto al abrir el formulario de creación de un evento y DEBE ofrecer el catálogo de canciones de la banda para seleccionarlas.

#### Scenario: El formulario ofrece el repertorio activado por defecto con el catálogo de canciones

- **GIVEN** Marta tiene el rol de Líder de Alabanza y el catálogo de la banda tiene 20 canciones de ejemplo
- **WHEN** Marta abre el formulario de creación de un evento de ensayo
- **THEN** el bloque de repertorio aparece activado por defecto
- **AND** Marta puede ver las 20 canciones del catálogo para seleccionarlas

### Requirement: Registrar solo las canciones seleccionadas

El sistema DEBE registrar las canciones seleccionadas y asociarlas al evento, sin asociar las canciones que no fueron seleccionadas.

#### Scenario: El líder crea un evento con canciones seleccionadas

- **GIVEN** Marta tiene el rol de Líder de Alabanza y el catálogo tiene las canciones «Cuán grande es Él» y «Sublime gracia»
- **WHEN** Marta crea un evento de ensayo para el sábado 14 de noviembre y selecciona esas dos canciones
- **THEN** el evento queda registrado con esas dos canciones en su repertorio
- **AND** el detalle del evento muestra las canciones seleccionadas

#### Scenario: Las canciones no seleccionadas no se asocian al evento

- **GIVEN** Marta tiene el rol de Líder de Alabanza y el catálogo tiene las canciones «Cuán grande es Él» y «Sublime gracia»
- **WHEN** Marta selecciona solo «Cuán grande es Él» al crear el evento del sábado 14 de noviembre
- **THEN** «Cuán grande es Él» queda en el repertorio del evento
- **AND** «Sublime gracia» no queda asociada al evento

### Requirement: Permitir eventos sin repertorio

El sistema DEBE permitir crear un evento sin canciones cuando el líder desactiva el bloque de repertorio o cuando deja la selección vacía, y DEBE indicar en el detalle que el evento no incluye repertorio.

#### Scenario: El líder crea un evento sin repertorio porque es una reunión

- **GIVEN** Marta tiene el rol de Líder de Alabanza y está creando un evento para una reunión de coordinación
- **WHEN** Marta desactiva el bloque de repertorio y crea el evento para el sábado 14 de noviembre
- **THEN** el evento queda registrado sin canciones
- **AND** el detalle del evento indica que no incluye repertorio

#### Scenario: El líder deja el repertorio activado pero no selecciona canciones

- **GIVEN** Marta tiene el rol de Líder de Alabanza
- **WHEN** Marta crea un evento para el sábado 14 de noviembre con el bloque de repertorio activado y sin seleccionar canciones
- **THEN** el evento queda registrado sin canciones
- **AND** el detalle del evento indica que no incluye repertorio

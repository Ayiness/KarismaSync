# Spec Delta — perfil-instrumental

## Purpose

Permitir que cada integrante de la banda registre y cambie su instrumento principal, para que el Líder de Alabanza lo vea al crear un evento de ensayo.

## ADDED Requirements

### Requirement: Registrar el instrumento principal

El sistema DEBE permitir que el integrante seleccione su instrumento principal del catálogo y DEBE mostrarlo al Líder de Alabanza al crear un evento de ensayo.

#### Scenario: El integrante registra su instrumento principal

- **GIVEN** Pedro es integrante de la banda y todavía no tiene un perfil instrumental
- **WHEN** Pedro selecciona guitarra eléctrica como su instrumento principal
- **THEN** el perfil de Pedro queda registrado con guitarra eléctrica como instrumento principal
- **AND** el Líder de Alabanza puede ver ese instrumento al crear un evento de ensayo

### Requirement: Cambiar el instrumento principal

El sistema DEBE permitir que el integrante reemplace su instrumento principal.

#### Scenario: El integrante cambia su instrumento principal

- **GIVEN** Pedro tiene registrado guitarra eléctrica como su instrumento principal
- **WHEN** Pedro cambia su instrumento principal a guitarra acústica
- **THEN** el perfil de Pedro queda con guitarra acústica como instrumento principal

### Requirement: Exigir un instrumento principal

El sistema NO DEBE registrar el perfil sin instrumento principal y DEBE informar al integrante.

#### Scenario: El integrante intenta registrar su perfil sin instrumento principal

- **GIVEN** Pedro es integrante de la banda y todavía no tiene un perfil instrumental
- **WHEN** Pedro intenta guardar su perfil sin indicar un instrumento principal
- **THEN** el perfil de Pedro no queda registrado
- **AND** Pedro es informado de que debe indicar un instrumento principal

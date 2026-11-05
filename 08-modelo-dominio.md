# Modelo de dominio
 
## Diagrama
![Modelo de dominio](./diagramas/modelo-dominio.png)
 
Archivo fuente: [`./diagramas/modelo-dominio.puml`](./diagramas/modelo-dominio.puml)
 
## Descripción de las clases
| Clase | Qué representa en el negocio | Atributos |
|-------|------------------------------|-----------|
| [Clase] | [Descripción de una línea] | [atributo1, atributo2] |
 
## Asociaciones
| Asociación | Clases | Multiplicidades | Justificación |
|------------|--------|-----------------|----------------|
| [verbo] | [ClaseA] – [ClaseB] | [1] a [0..*] | [Regla del negocio que la sustenta] |
 
## Decisiones de modelado
- [Roles que se modelaron como rol y no como clase, y por qué]
- [Uso de agregación o composición, con su justificación; o "no se usó"]

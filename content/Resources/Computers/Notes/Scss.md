---
tags:
  - Coding
  - WebDevelopment
---


## Variabili
```scss
$width: 5em;
```

## Liste
Gestiscono insiemi di valori come: margin: 10px 15px 0 0
Utili per poi essere usate su funzioni comode di elaborazione array. 
```scss
$margin: 10px 15px 0 0
```

## Maps
Analoghi agli array associativi.
```scss
$map: (key1: value1, key2: value2, key3: value3);
```

## Operazioni matematiche
Supporta addizione, sottrazione, moltiplicazione, divisione e modulo.
Il + può essere utilizzato per concatenare stringhe.

## &
Selettore che indica il selettore padre corrente
Se non ho un padre il valore di & sarà null. Posso usare questa cosa utilizzando il costrutto `@if`

```scss
@mixin does-parent-exist {
@if & {
&:hover {
color: red;
}
} @else {
a {
color: red;
}
}
}
```

## @extend
Usare quando una classe deve avere tutti gli stili di un’altra classe più i suoi stili specifici.

```scss
.hoverlink {
@extend a:hover;
}
a:hover {
text-decoration: underline;
}
```

Posso anche fare extend multipli

```scss
.error {
border: 1px #f00;
background-color: #fdd;
}
.attention {
font-size: 3em;
background-color: #ff0;
}
.seriousError {
@extend .error;
@extend .attention;
border-width: 3px;
}
```

## Placeholder
Se voglio creare una classe che viene utilizzata **solo** come `@extend` e mai da sola devo usare i placeholder selectors. `#` o `.` sono sostituiti dal `%`, in questo modo non vengono compilati da soli.

```scss
%extreme {
color: blue;
}
.notice {
@extend %extreme;
}
```

## @if

Data un’espressione *SassScript*, se questa risulta vera verrà compilato lo stile sottostante (tra {} )

```scss
$type: monster;
p {
@if $type == ocean {
color: blue;
} @else if $type == matador {
color: red;
} @else if $type == monster {
color: green;
} @else {
color: black;
}
}
```

## @each

Esegue delle istruzioni data una lista in ingresso. Usata nella forma `@each $var in <list or map>`.

```scss
@each $animal in puma, sea-slug, egret, salamander {
.#{$animal}-icon {
background-image: url('/images/#{$animal}.png');
}
}
@each $animal, $color, $cursor in (puma, black, default),
(sea-slug, blue, pointer),
(egret, white, move) {
.#{$animal}-icon {
background-image: url('/images/#{$animal}.png');
border: 2px solid $color;
cursor: $cursor;
}
}
```

## @mixin

Definisco delle funzioni tramite la stringa @mixin e vengono richiamate con `@include`.

```scss
@mixin sexy-border($color, $width: 1in) {
border: {
color: $color;
width: $width;
style: dashed;
}
}
p { @include sexy-border(blue); }
h1 { @include sexy-border(blue, 2in); }
```

Posso chiamare un mixin con un passaggio esplicito di parametri (array associativo) per una più facile lettura

```scss
p { @include sexy-border($color: blue); }
h1 { @include sexy-border($color: blue, $width: 2in); }
Posso avere anche un numero arbitrario di argomenti al mixin
@mixin box-shadow($shadows...) {
-moz-box-shadow: $shadows;
-webkit-box-shadow: $shadows;
box-shadow: $shadows;
}

.shadows {
@include box-shadow(0px 4px 5px #666, 2px 6px 10px #999);
}
```

## Funzioni

Per le operazioni matematiche su variabili posso definire funzioni custom con la parole 

```scss
@function
$grid-width: 40px;
$gutter-width: 10px;

@function grid-width($n) {
@return $n * $grid-width + ($n - 1) * $gutter-width;
}
#sidebar { width: grid-width(5); }
```
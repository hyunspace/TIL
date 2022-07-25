# CSS Layout

## with Block & Inline Block



## with Floats

#### `float`

![image-20220411011647581](05_Layout.assets/image-20220411011647581.png)

#### `margin-rigth` & `margin-bottom`

![image-20220411011920601](05_Layout.assets/image-20220411011920601.png)

* `TRouBLe` == **Top Right Bottom Left**

  ```css
  margin: 0 rem; 1rem 0;
  ```

<br/>

#### `article` & `auto margin`

![image-20220411012557479](05_Layout.assets/image-20220411012557479.png)

* `margin: 0 auto;`

  : calculate how much extra space we have and divide it in two and stick half on each side of the box(in this case, article).

<br/>

#### Image Right & Clear

![image-20220411013036126](05_Layout.assets/image-20220411013036126.png)

* If you float, you must clear!

* This should go on a parent

  ```css
  article:after {
      content: "";
      display: table;
      clear: both;
  }
  ```

  => Adding empty content and displaying it as a table

  ![image-20220411013412718](05_Layout.assets/image-20220411013412718.png)

<br/>

## with Flexbox

#### `Display: Flex;`

* Flexbox is all about parents and children!

  ![image-20220412235600397](05_Layout.assets/image-20220412235600397.png)

  * `<ul>` is the **parent** and the **flex container**
  * `<li>` is the **children** and the **flex items**
  * No grandparent or grandchildren. They must be parents and children in order for Flexbox to work.

 <br/>

#### Direction & Wrap with Flex Flow

* `flex-flow: row wrap;`

![image-20220413000520216](05_Layout.assets/image-20220413000520216.png)

* `flex-flow: column wrap;`

![image-20220413000530475](05_Layout.assets/image-20220413000530475.png)

* `nowrap` : the width is gonna be flexible

<br/>

#### Justify Content

* `justify-content: flex-start:`

* [a guide to flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
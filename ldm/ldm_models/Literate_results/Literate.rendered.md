# None


!! Error: Name is missing

## Preliminaries - the basic structure of the model

In Literate Data Modeling, the main components of interest are typically
Classes, Attributes, Models, and Subjects. However, to streamline the model and
promote reusability, we introduce a supertype called Component. By defining
common attributes and behaviors in the Component class, we can inherit them in
the subclasses, ensuring consistency and reducing duplication throughout the
model.


We present the Component class first because it is a best practice in modeling
to introduce supertypes before their subtypes. This approach allows readers to
understand the general concepts and shared properties before delving into the
specifics of each specialized component.


_ **Component** - An element or building block of the literate data model

- ***normalName*** - the name of the component, not in camel case (optional
reference String)

- ***name*** - The name of the component (optional reference CamelName)

- ***qualifiedName*** (optional reference QualifiedCamel)

- ***abbreviatedName*** - a short form of the component's name, used for cross
references and improved readability. (optional reference CamelName)

Example: "LDM" is the short form of "Literate Data Model".
- ***oneLiner*** - A brief, one-line definition or description of the component,
suitable for use in a descriptive table of contents. _ (optional reference
RichLine)


!! Warning: oneLiner is too long. (116 chars).

- ***elaboration*** - A more detailed explanation or discussion of the component
_ (optional reference RichText)

__ _For Machinery_ - mechanical attributes ()

- ***isEmbellishment*** - Indicates whether this component is an embellishment
added during post-parsing processing _ (optional reference Boolean)

Note: This attribute is set to true for components that are automatically
generated or added during the fleshing out, review, or rendering processes, such
as implied attributes or suggested model elements. It helps distinguish
embellishments from the core model elements defined in the original LDM source.

!! Warning: oneLiner is too long. (91 chars).

_ **AnnotationType** - a kind of note, or aside, used to call attention to
additional information about some Component.

Note: Each LDM declares a set of Annotation Types, with defined labels, emojis,
and clearly documented purposes. These are *recognized* or *registered*
Annotation Types.

!! Warning: oneLiner is too long. (96 chars).

_based_on_: Literate Data Model
- ***emoji*** - an emoji (optional reference Emoji)

- ***emojiName*** - an emoji (optional reference String)

- ***emojiUnicode*** - the Unicode for the emoji (optional reference Unicode)

- ***label*** - A short label to indicate the purpose of the annotation _
(optional reference CamelName)

- ***plural*** - the plural form of the label (optional reference UpperCamel)

- ***Purpose*** - the intended reason for the annotation.


!! Error: No value for data_type_clause

_ **ValueType Annotation A note or comment associated with a model element**

_based_on_: Component
- ***annotationType*** (optional reference Annotation Type)

Note: An Annotation is considered to *recognized* if the label is associated
with an Annotation Type. otherwise it is *ad hoc*.
- ***label*** - A short label to indicate the purpose of the annotation _
(optional reference CamelName)

But any short label is valid.


- ***Emoji*** (optional reference Emoji)

- ***content*** - The content or body of the annotation (optional reference
RichText)

__ _For Machinery_ ()

- ***isEmbellishment*** - Indicates whether this annotation is an embellishment
added during post-parsing processing _ (optional reference Boolean)

Note: This attribute is set to true for annotations that are automatically
generated or added during the fleshing out, review, or rendering processes, such
as suggestions, issues, or diagnostic messages. It helps distinguish
embellishment annotations from the annotations defined in the original LDM
source.

!! Warning: oneLiner is too long. (92 chars).

## The Model and its Subjects

_ **LiterateDataModel** - A representation of a domain's entities, attributes,
and relationships, along with explanatory text and examples


!! Warning: oneLiner is too long. (112 chars).

_plural_:  LiterateDataModels

_subtype_of_: Component Subtypes
- ***name*** (optional reference UpperCamel)

- ***allSubjects*** - list of all classes in the model, as ordered in the
definition of the model. (optional List of reference Classes)

- ***allClasses*** - list of all classes in the model, as ordered in the
definition of the model. (optional List of reference Classes)

__ _Modeling Configuration_ ()

- ***annotationTypes*** (optional List of reference AnnotationTypes)

- ***Preferred Coding Language*** - the recommended lanquage  for expressing
derivation, defaults, and constraints (optional reference Coding Language)

- ***alternate Coding Languages*** (optional List of reference Coding Languages)

- ***Preferred Template Language*** - the recommended lanquage  for expressing
derivation, defaults, and constraints (optional reference Template Language)

- ***alternate Template Languages*** (optional List of reference Template
Languages)

- ***aiFunctions*** - A list of functions that require sophisticated AI-powered
implementation * (optional List of reference String)

_ **Subject A specific topic or theme within the model**

Subjects are the chapters an sections of the model.

+ A subject need not contain any Classes if it’s just expository.


_plural_:  Subjects

_subtype_of_: Component Subtypes
_dependent_of_: LiterateDataModel
- ***name*** (optional reference UpperCamel)

- ***parentSubject*** - The parent subject, if any, under which this subject is
nested _ (optional reference Subject)

- ***Classes*** - The major classes related to this subject, in the order in
which they should be presented _ (optional List of reference Classes)

Issue: define chapter, section, subsection as levels?

!! Warning: oneLiner is too long. (91 chars).

- ***Each Class should be followed first by the classes that are dependent on
it, and then***


!! Error: No value for data_type_clause

- ***By its subtype classes.***


!! Error: No value for data_type_clause

- ***childSubjects*** - Any child subjects nested under this subject, in the
order in which they should be presented _ (optional List of reference Subjects)

***DSL***:  the Classes within a Subject are always displayed before the
childSubjects.



!! Warning: oneLiner is too long. (94 chars).

_inverse_: [_Subject_](Subject)_._parentSubject.
_ **SubjectArea A main topic or area of focus within the model, containing
related subjects and classes**

_plural_:  SubjectAreas

_subtype_of_: Subject Subtypes
_where_:  parentSubject is absent

### Classes

_ **Class** - A key entity or object type in the model, often corresponding to a
real-world concept

_plural_:  Classes

_subtype_of_: Component Subtypes
_Constraint_:  Within each Class, attribute names must be unique.

_english_: 


- ***pluralForm*** - the normal English plural form of the name of the Class
(optional reference UpperName)

Might be Books for the Book class or other regular plurals.

+ But also might be People for Person.


Note: When inputting a model, you will rarely need to specify the plural form.
The input program will just look it up.
- ***basedOn*** - the Class or Classes on which this class is dependent
(optional Set of reference Classes)

This is solely based on **Existence Dependency**. A true dependent entity cannot
logically exist without the related parent entity. For instance, an Order Item
cannot exist without an Order. If removing the parent entity logically implies
removing the dependent entity, then it is a dependent entity.


Note: that basedOn and dependentOf are being used synonymousle in this
metamodel.
- ***supertypes*** - The parent class (optional reference es)

- ***subtypings*** - the criteria, or dimensions, by which the class can be
divided into subtypes (optional List of reference Subtypings)

Example: in a library model, the `Book` class could have subtypings based on
genre (e.g., Fiction, Non-fiction), format (e.g., Hardcover, Paperback), or
subject (e.g., Science, History).
- ***subtypes*** - Any subtypes or specializations of this class based on it’s
subtypings. _ (optional List of reference Classes)

Example: For instance, using the `Book` example, the subtypes could include
`FictionBook`, `Non-fictionBook`, `HardcoverBook`, `PaperbackBook`,
`ScienceBook`, and `HistoryBook`.
- ***attributes*** - The attributes or properties of the class, in the order in
which they should be presented _ (optional List of reference Attributes)

- ***attributeSections*** - additional attributes or properties of the class,
grouped for clarity and elaboration.  _ (optional List of reference
AttributeSections)

- ***constraints*** - Any constraints, rules, or validations specific to this
class _ (optional List of reference Constraints)

Note: Constraints may be expressed on either the Class or the Attribute. Always?
- ***methods*** - Any behaviors or operations associated with this class _
(optional List of reference Methods)

__ _Implied Attributes_ ()

- ***dependents*** - the Classes which are basedOn this Class (optional Set of
reference Classes)

_inverse_: [_Class_](Class)_._basedOn
- ***UniqueKeys*** (optional Set of reference UniqueKeys)

_inverse_: [_UniqueKey_](UniqueKey)_._basedOn
_ **Subtyping** - a way in which subtypes of a Class may be classified

_dependent_of_: Class
- ***name*** (optional reference Upper Name)

- ***is exclusive*** (optional reference Boolean)

- ***is exhaustive*** (optional reference Boolean)

- ***classes*** (optional List of reference Classes)

***DSL***:  Shown in the DSL as

+ > Subbtypes: byBrand - Brand1, Brand2,... (non exclusive, exhaustive)

+ on the super class. And as

+ > Subtype of: SuperClass byBrand

+ on the subclass.


Note: every class can have an unnamed subtyping.
_ **ValueType**

_subtype_of_: Class. Subtypes
_ **Reference Type**

_subtype_of_: Class. Subtypes
_ **CodeType A data type or enumeration used in the model**

Note: Often, a CodeType will be assigned to just one attribute in the model.  In
such cases, there's no need to declare a new Code Type and invent a name for it.
Instead:
_subtype_of_: ValueType. Subtypes
- ***List the code values as a bulletted list inside the description of the
attribute in the form ‘code description’***

- ***A Code Type will be created with the name [class][attribute]Code and the
code values listed. That CodeType will be marked as isCaptive.***

- ***isCaptive*** - the code type was implied by use in an attribute and is only
used for that attribute (optional reference Boolean)

_ **Code Value**

A possible value for an enumerated data class  DependentOf: CodeType
- ***code*** - A short code or abbreviationi for the value _ (optional reference
NameString)

- ***description*** - an explanation of what the code means (optional reference
RichText)

_ **Key** - a list of attributes of a class

_subtype_of_: Component Subtypes
_dependent_of_: Class
- ***keyAttributes*** - the attributes of the base Class. (optional List of
reference Attributes)

Issue: need ascending descending to support index keys or ordering keys.
_ **UniqueKey** - a list of attributes on which instances of the base class may
be keyed.

Note: order unimportant for Unique Keys.
_subtype_of_: Key Subtypes
## Attributes

_ **Attribute Section** - a group of attributes for a class that merit a shared
explanation.

_subtype_of_: Component. Subtypes
_based_on_: Class
- ***isOptional*** - whether the attributes in this section, taken together, are
optional. (optional reference Boolean)

If the Attribute Section is required,then each Attribute within the sectional is
optional ot required, depending on how it is marked.

+ &nbsp;

+ But if the Arrribute Section is optional each attribute in the section is only required if any attribute in the section is ptresent.


_ **Attribute A property or characteristic of a class**

_plural_:  Attributes

_subtype_of_: Component Subtypes
_based_on_: AttributeSection
- ***name*** (optional reference Lower Camel)

_overrides_: [_CamelName_](CamelName)_._
- ***dataType*** - The kind of object to which the attribute refers.  _
(optional reference DataType)

But,


- ***List of Editions***


!! Error: No value for data_type_clause

- ***Set of Edition***


!! Error: No value for data_type_clause

- ***... and more complicated cases.***

See: the section below on Data Type Specifiers.

!! Error: No value for data_type_clause

__ _Cardinalities._ ()

- ***isOptional*** - Indicates whether the attribute must have a value for every
instance of the class _ (optional reference Boolean)

- ***cardinality*** - The cardinality of the relationship represented by the
attribute _ (optional reference CardinalityCode)

For example:
- ***author*** (optional value Invented Name)

- ***books*** (optional value Invented Name)

Note: how this works with optionality
__ _Inverse Attributes_ ()

- ***isInvertible*** (optional reference Boolean)

- ***inverseClass*** - the class which contains, or would contain the inverse
attribute (optional reference Class)

- ***inverseAttribute*** (optional reference Attribute)

- ***inverseIsOptional*** (optional reference Attribute)

_ **Formulas**

- ***default*** - The rule or formula for calculating the value, if no value is
supplied Now running to a second line with the parenthentical on yet a third
line (optional reference Derivation)

Note: even when an Attribute has a default derivation, there’s no guarantee that
every instance will have an assigned value. Example needed.

!! Warning: oneLiner is too long. (143 chars).

- ***derivation*** - For derived attributes, the rule or formula for calculating
the value _ (optional reference Derivation)

Issue: on insert vs on access?
- ***constraints*** - Any validation rules specific to this attribute _
(optional List of reference Constraints)

Note: from Class.constraints
__ _Override Tracking_ ()

- ***Overrides***


!! Error: No value for data_type_clause

_ **ValueType Derivation A rule or formula for deriving the value of an
attribute**

_plural_:  Derivations

- ***statement*** - An English language statement of the derivation rule _
(optional reference RichText)

- ***expression*** - The formal expression of the derivation in a programming
language _ (optional reference CodeExpression)

_ **ValueType Constraint A rule, condition, or validation that must be satisfied
by the model**

_plural_:  Constraints

_subtype_of_: Component Subtypes
- ***statement*** - An English language statement of the constraint _ (optional
reference RichText)

- ***expression*** - The formal expression of the constraint in a programming
language (optional value Invented Name)

- ***severity*** (optional reference Code)

- ***None*** - **Warning** - nothing fatal; just a caution


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***None*** - **Error** - serious. Fix now


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***Message*** (optional reference Template)

_ **Class Constraint**

_subtype_of_: Constraint Subtypes
_based_on_: Class.
_ **Attribute Constraint**

_subtype_of_: Constraint Subtypes
_based_on_: Attribute
_ **CodeExpression**

- ***Language*** - the programming language (optional reference Code)

- ***None*** - OCL: Object Constraint Language


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***None*** - Java: Java


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***Expression*** (optional reference String)

## Methods

_ **Method A behavior or operation associated with a class**

_plural_:  Methods

_subtype_of_: Component Subtypes
- ***parameters*** - The input parameters of the method _ (optional List of
reference Parameters)

- ***returnType*** - The data type of the value returned by the method _
(optional reference DataType)

_ **Parameter An input to a method**

_plural_:  Parameters

_subtype_of_: Component Subtypes
- ***type*** - The data type of the parameter _ (optional reference DataType)

- ***cardinality*** - The cardinality of the parameter (optional value Invented
Name)

## Data Types

*ValueType*:**Data Type**


_ **Simple Data Type SubtpeOf DataType**

- ***coreClass*** (optional reference Class)

_ **Complex Data Type**

- ***aggregation*** (optional reference Aggregating Operator)

- ***aggregatedTypes*** (optional List of reference DataTypes)

_ **Aggregating Operator**

- ***Name*** (optional reference Code)

- ***None*** - **SetOf**


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***None*** - **ListOf**


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***None*** - **Mapping**


!! Error: Name is missing
!! Error: No value for data_type_clause

- ***arity*** (optional reference Integer)

- ***spelling*** (optional reference Template)

## Low level Data Types

insert Camel Case.md


_ **ValueType CamelName**

A short string without punctuation or spaces, suitable for names, labels, or
identifiers and presented in camel case.


_subtype_of_: String Subtypes
- ***value the string*** (optional reference String)

Example: "firstName", "orderDate", "customerID"
ModelingNote: * *CamelName* is presented here, just after its first usage by
another class (Component), to provide context and understanding before it is
used further in the model.
_ **UpperCamel** - a CamelName that begins with a capital letter

Example: _ "Customer", "ProductCategory", "PaymentMethod"
_subtype_of_: CamelName Subtypes
_where_:  content begins with an upper case letter.

_ **LowerCamel** - a CamelName that begins with a lower case letter

Example: "firstName", "orderTotal", "shippingAddress"
_subtype_of_: CamelName Subtypes
_where_:  content begins with a lower case letter.

_ **Qualified Camel** - an expression consisting of Camel Names separated by
periods

_subtype_of_: String Subtypes
_Constraint_:  content consists of CamelNames, separated by periods.  Each of the camel names must be Upper Camel except, possibly, the first.

_english_: 


_ **RichText.  A string with markup for block level formatting.**

_subtype_of_: String Subtypes
- ***value*** - the string content (optional reference string)

- ***format*** - the rich text coding language used (optional reference Code)

- ***HTML***


!! Error: No value for data_type_clause

- ***MarkDown***


!! Error: No value for data_type_clause

_ **RichLine** - String with markup for line level formatting.

_subtype_of_: RichText Subtypes
- ***value*** - the string content (optional reference string)

_ **PrimitiveType**

Values:
_subtype_of_: ValueType
A basic Subtypes, built-in data type Subtypes
## Appendices Insert More Sidebars.md Insert Overrides.md insert LDM Intro.md
Insert OCL.md Insert Camel Case.md

### Annotation Types Used

These are the recognized Annotation Types for the LDM model.


And this is how you register the AnnotationTyped for a model. By including this
sort of array in the DSL document for the model.


```typescript
interface AnnotationType {
label: string;
emoji: string;
emojiName: string;
emojiUnicode: string;
purpose: string;
}
// LINK: LiterateDataModel.annotationTypes
const annotationTypes: AnnotationType[] = [
{
label: "Error",
emoji: "",
emojiName: "cross_mark",
emojiUnicode: "U+274C",
purpose: "Indicates a critical error or failure in the model."
},
{
label: "Warning",
emoji: "",
emojiName: "warning",
emojiUnicode: "U+26A0",
purpose: "Indicates a potential issue or warning in the model."
},
{
label: "Note",
emoji: "",
emojiName: "blue_book",
emojiUnicode: "U+1F4D8",
purpose: "Provides additional context, explanations, or clarifications for the annotated element."
},
{
label: "Issue",
emoji: "",
emojiName: "warning",
emojiUnicode: "U+26A0",
purpose: "Highlights a potential issue or error that needs to be addressed or resolved."
},
{
label: "Question",
emoji: "",
emojiName: "question",
emojiUnicode: "U+2753",
purpose: "Raises a question or seeks further clarification about the annotated element."
},
{
label: "Suggestion",
emoji: "",
emojiName: "bulb",
emojiUnicode: "U+1F4A1",
purpose: "Provides a suggestion or recommendation for improving the model or the annotated element."
},
{
label: "Info",
emoji: "",
emojiName: "information_source",
emojiUnicode: "U+2139",
purpose: "Offers relevant information, facts, or details about the annotated element."
},
{
label: "Todo",
emoji: "",
emojiName: "pushpin",
emojiUnicode: "U+1F4CC",
purpose: "Indicates a pending task, action item, or future work related to the annotated element."
},
{
label: "Reference",
emoji: "",
emojiName: "globe_with_meridians",
emojiUnicode: "U+1F310",
purpose: "Provides a reference or link to an external resource or documentation."
},
{
label: "See",
emoji: "",
emojiName: "mag",
emojiUnicode: "U+1F50D",
purpose: "Indicates a cross-reference to another relevant element within the model."
}
];
```

===


## Appendices Insert More Sidebars.md Insert Overrides.md insert LDM Intro.md
Insert OCL.md Insert Camel Case.md

== content to add



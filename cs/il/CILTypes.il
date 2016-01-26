.assembly extern mscorlib
{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 )
  .ver 4:0:0:0
}

.assembly CILTypes
{
  .ver 1:0:0:0
}
.module CILTypes.dll

.namespace Andersc.MyNamespace
{
  .class public interface IMyInterface {}

  .class public MyBaseClass {}

  .class public MyDerivedClass
    extends Andersc.MyNamespace.MyBaseClass
    implements Andersc.MyNamespace.IMyInterface {}

  .class public interface IAnotherInterface
    implements Andersc.MyNamespace.IMyInterface {}

  // A struct def is always sealed.
  .class public sealed MyStruct
    extends [mscorlib]System.ValueType {}

  // Or use value attribute
  .class public sealed value MyStruct2 {}

  // An enum
  .class public sealed MyEnum
    extends [mscorlib]System.Enum {}

  // Or use enum attribute
  .class public sealed enum MyEnum2 {}
}

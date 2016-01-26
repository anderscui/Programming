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

  .class public MyBaseClass 
  {
    .field private string stringField = "myclass"
    .field private int32 intField = int32(42)

    .method public hidebysig specialname rtspecialname
      instance void .ctor(string s, int32 i) cil managed
    {
      // TODO  
    }

    .method public hidebysig specialname
      instance string get_TheString() cil managed
    {
      // TODO
    }

    .method public hidebysig specialname
      instance void set_TheString(string 'value') cil managed
    {
      // TODO
    }

    .property instance string TheString()
    {
      .get instance string
        Andersc.MyNamespace.MyBaseClass::get_TheString()
      .set instance void
        Andersc.MyNamespace.MyBaseClass::set_TheString(string)
    }

    .method public hidebysig static void MyMethod(int32 inputInt,
      int32& refInt,
      class [mscorlib]System.Collections.ArrayList ar,
      [out] int32& outputInt) cil managed
    {
      // TODO
    }

    .method public hidebysig instance void Speak() cil managed
    {
      .maxstack 1
      ldstr "hello"
      call void [mscorlib]System.Console::WriteLine(string)
      ret
    }

    .method public hidebysig static void 
      MyLocalVars() cil managed
    {
      .maxstack 8
      .locals init ([0] string myStr, [1] int32 myInt,
        [2] object myObj)
      ldstr "CIL code is fun"
      // pop off current value and store in local var [0]
      stloc.0

      // load a constant
      ldc.i4 33
      stloc.1

      // create a new obj
      newobj instance void [mscorlib]System.Object::.ctor()
      stloc.2

      ret
    }
  }

  .class public MyDerivedClass
    extends Andersc.MyNamespace.MyBaseClass
    implements Andersc.MyNamespace.IMyInterface 
  {
    // static method
    .method public hidebysig static int32 Add(int32 a, int32 b) cil managed
    {
      // C#: return a + b
      .maxstack 2
      ldarg.0
      ldarg.1
      add
      ret
    }
  }

  .class public interface IAnotherInterface
    implements Andersc.MyNamespace.IMyInterface {}

  // A struct def is always sealed.
  .class public sealed MyStruct
    extends [mscorlib]System.ValueType {}

  // Or use value attribute
  .class public sealed value MyStruct2 {}

  // An enum
  .class public sealed MyEnum
    extends [mscorlib]System.Enum 
    {
      .field public static literal valuetype
        Andersc.MyNamespace.MyEnum A = int32(0)
      .field public static literal valuetype
        Andersc.MyNamespace.MyEnum B = int32(1)
      .field public static literal valuetype
        Andersc.MyNamespace.MyEnum C = int32(2)
    }

  // Or use enum attribute
  .class public sealed enum MyEnum2 {}
}

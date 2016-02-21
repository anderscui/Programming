We can examine the types within a project's referenced set of assemblies using **Object Browser** of VS. 
Furthermore, external tools such as ildasm allow us to peek into the underlying CIL code, type metadata etc.

We are also able to programmatically obtain this info using the `System.Reflection` namespace.

# The Necessity of Type Metadata

Numerous .NET technologies, such as WCF, and serialization require the ability to discover the format of types at runtime.
And cross-language interoperability, numerous compiler services, and an IDE's IntelliSense capabilities all rely
on a concrete description of *type*.

* TypeDef #n token
* TypeRef #n token
* Method #n
* Property #n

* Assembly
* AssemblyRef

* User Strings (String Literals)

# Understanding Reflection

* Assembly
* AssemblyName
* EventInfo
* FieldInfo
* MemberInfo
* MethodInfo
* Module
* ParameterInfo
* PropertyInfo

## System.Type class

# Understanding Late Binding

**late binding**: create an instance of a given type and invoke its members at runtime without having hardcoded compile-time knowledge of its existence.

late binding does have a criticla role in any **extendable application** you may be building.

## `System.Activator` class

The `System.Activator` class is the key to the .NET late-binding process.

# Understanding the Role of .NET Attributes

In a nutshell, attributes are nothing more than code annotations that can be applied to a given type, member, assembly, or module.

* CLSCompliant
* DllImport
* Obsolete
* Serializable
* NonSerialized
* ServiceContract

When you apply attributes in your code, the embedded metadata is essentially useless until another piece of code explicitly reflects over the info.


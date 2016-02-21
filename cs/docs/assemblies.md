
# The Role of .NET Assemblies

Despite the .NET assemblies have the same file extensions (*.exe or *.dll) as previous Windows binaries, 
they have **little in common** with those files under the hood.

## Assemblies promote code reuse

Regardless of how a code library is packaged, the .NET platform allows you to reuse types in a language-independent manner.

## Assemblies establish a type boundary

MyAsm.Class vs. YourAsm.Class

## Assemblies are versionalbe units

Version: <major>.<minor>.<build>.<revision>

Assemblies can be *strongly named*.

## Assemblies are self-describing

**manifest** file + every contained type, so Windows system registry is not needed to resolve.

## Assemblies are configurable

* private
* shared (GAC)

# Format of a .NET Assembly

* A Windows file header (>dumpbin /headers CarClieint.dll)
* A CLR file header (>dumpbin /clrheader CarClieint.dll)
* CIL code
* Type metadata
* An assembly manifest
* Optional embedded resources (satellite assemblies)

# Private Assemblies

Private assemblies must be located within the same directory as the client app that's using them or a sub dir thereof.

## Identity

friendly name (module name) + version number.

## Probing process

## Config

`<assemblyBinding><probing /></assemblyBinding>`

### The Role of the App.config File


# Shared Assemblies

## The global assembly cache

* /c/Windows/assembly (before 4.0)
* /c/Windows/Microsoft.NET/assembly/GAC_MSIL (higher) -> v4.0_4.0.0.0__b77a5c561934e089

## Strong names

Before you can deploy an assembly to the GAC, you must assign it a strong name, 
which is used to uniquely identify the publisher of a given .NET binary.

# <codeBase> config section


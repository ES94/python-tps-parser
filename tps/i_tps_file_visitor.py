"""
Este archivo está destinado a las interfaces. Por definición, las interfaces 
no son necesarias en Python. Esto se debe a que Python tiene una herencia 
múltiple adecuada, y también ducktyping, lo que significa que los lugares 
donde debe tener interfaces en C#, no tiene que tenerlas en Python.
En primera instancia, se copiarán la insterfaces de C# tal y como están. 
Luego, se procederá a modificar el proyecto en Python de modo tal que cumpla 
con las características que poseen las interfaces en el proyecto de C#.
"""

# Código original del proyecto en C#

# using TpsParse.Tps.Record;
#
# namespace TpsParse.Tps
# {
#     public interface ITpsFileVisitor<out T>
#     {
#         T Visit(DataRecord record);
#         T Visit(EmptyRecord record);
#         T Visit(IndexRecord record);
#         T Visit(MemoRecord record);
#         T Visit(MetadataRecord record);
#         T Visit(TableDefinitionRecord record);
#         T Visit(TableNameRecord record);
#         T Visit(TpsFile file);
#     }
# }
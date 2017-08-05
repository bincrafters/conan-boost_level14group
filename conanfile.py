from conans import ConanFile, tools, os


class BoostLevel14GroupConan(ConanFile):
    name = "Boost.Level14Group"
    version = "1.64.0"
    generators = "txt"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-level14group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing"
    requires = "Boost.Algorithm/1.64.0@bincrafters/testing", \
        "Boost.Any/1.64.0@bincrafters/testing", \
        "Boost.Array/1.64.0@bincrafters/testing", \
        "Boost.Assert/1.64.0@bincrafters/testing", \
        "Boost.Bind/1.64.0@bincrafters/testing", \
        "Boost.Concept_Check/1.64.0@bincrafters/testing", \
        "Boost.Config/1.64.0@bincrafters/testing", \
        "Boost.Conversion/1.64.0@bincrafters/testing", \
        "Boost.Core/1.64.0@bincrafters/testing", \
        "Boost.Detail/1.64.0@bincrafters/testing", \
        "Boost.Dynamic_Bitset/1.64.0@bincrafters/testing", \
        "Boost.Exception/1.64.0@bincrafters/testing", \
        "Boost.Filesystem/1.64.0@bincrafters/testing", \
        "Boost.Foreach/1.64.0@bincrafters/testing", \
        "Boost.Function/1.64.0@bincrafters/testing", \
        "Boost.Functional/1.64.0@bincrafters/testing", \
        "Boost.Integer/1.64.0@bincrafters/testing", \
        "Boost.Iterator/1.64.0@bincrafters/testing", \
        "Boost.Lambda/1.64.0@bincrafters/testing", \
        "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
        "Boost.Math/1.64.0@bincrafters/testing", \
        "Boost.Move/1.64.0@bincrafters/testing", \
        "Boost.Mpl/1.64.0@bincrafters/testing", \
        "Boost.Multi_Index/1.64.0@bincrafters/testing", \
        "Boost.Optional/1.64.0@bincrafters/testing", \
        "Boost.Parameter/1.64.0@bincrafters/testing", \
        "Boost.Preprocessor/1.64.0@bincrafters/testing", \
        "Boost.Property_Tree/1.64.0@bincrafters/testing", \
        "Boost.Python/1.64.0@bincrafters/testing", \
        "Boost.Random/1.64.0@bincrafters/testing", \
        "Boost.Range/1.64.0@bincrafters/testing", \
        "Boost.Serialization/1.64.0@bincrafters/testing", \
        "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
        "Boost.Spirit/1.64.0@bincrafters/testing", \
        "Boost.Static_Assert/1.64.0@bincrafters/testing", \
        "Boost.System/1.64.0@bincrafters/testing", \
        "Boost.Test/1.64.0@bincrafters/testing", \
        "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
        "Boost.Tti/1.64.0@bincrafters/testing", \
        "Boost.Tuple/1.64.0@bincrafters/testing", \
        "Boost.Type_Traits/1.64.0@bincrafters/testing", \
        "Boost.Type_Traits/1.64.0@bincrafters/testing", \
        "Boost.Typeof/1.64.0@bincrafters/testing", \
        "Boost.Unordered/1.64.0@bincrafters/testing", \
        "Boost.Utility/1.64.0@bincrafters/testing", \
        "Boost.Variant/1.64.0@bincrafters/testing", \
        "Boost.Xpressive/1.64.0@bincrafters/testing"

    # Bimap Dependencies
    # concept_check5 config0 core2 functional5 iterator5 lambda6 mpl5 multi_index12 preprocessor0
    # property_map14 serialization11 static_assert1 throw_exception2 type_traits3 utility5

    # Disjoint_Sets Dependencies
    # graph14

    # Graph Dependencies
    # algorithm9 any6 array3 assert1 bimap14 bind3 concept_check5 config0 conversion5 core2 detail5 disjoint_sets14
    # foreach8 function5 functional5 graph_parallel14 integer3 iterator5 lexical_cast8 math8 move3 mpl5 multi_index12
    # optional5 parameter10 preprocessor0 property_map14 property_tree13 random9 range7 serialization11 smart_ptr4
    # spirit11 static_assert1 test10 throw_exception2 tti6 tuple4 type_traits3 typeof5 unordered8 utility5 xpressive9

    # Graph_Parallel Dependencies
    # assert1 concept_check5 config0 core2 detail5 disjoint_sets14 dynamic_bitset12 filesystem8 foreach8 function5
    # functional5 graph14 iterator5 lexical_cast8 mpi14 mpl5 optional5 property_map14 random9 serialization11 smart_
    # ptr4 static_assert1 tuple4 type_traits3 variant9

    # Mpi Dependencies
    # assert1 config0 core2 function5 graph14 integer3 iterator5 mpl5 optional5 property_map14 python9 serialization11
    # smart_ptr4 static_assert1 throw_exception2 type_traits3

    # Property_Map Dependencies
    # any6 assert1 bind3 concept_check5 config0 core2 function5 iterator5 lexical_cast8 mpi14 mpl5 multi_index12
    # optional5 serialization11 smart_ptr4 static_assert1 throw_exception2 type_traits3 utility5

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/bimap"))     

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/disjoint_sets"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/graph"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/graph_parallel"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/mpi"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/property_map"))
               
    def package(self):

        bimap_dir = os.path.join(self.build_folder, "bimap", "include")
        self.copy(pattern="*", dst="include", src=bimap_dir)

        disjoint_sets_dir = os.path.join(self.build_folder, "disjoint_sets", "include")
        self.copy(pattern="*", dst="include", src=disjoint_sets_dir)
        
        graph_dir = os.path.join(self.build_folder, "graph", "include")
        self.copy(pattern="*", dst="include", src=graph_dir)

        graph_parallel_dir = os.path.join(self.build_folder, "graph_parallel", "include")
        self.copy(pattern="*", dst="include", src=graph_parallel_dir)

        mpi_dir = os.path.join(self.build_folder, "mpi", "include")
        self.copy(pattern="*", dst="include", src=mpi_dir)

        property_map_dir = os.path.join(self.build_folder, "property_map", "include")
        self.copy(pattern="*", dst="include", src=property_map_dir)
        

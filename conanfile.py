from conans import ConanFile, tools, os


class BoostLevel14GroupConan(ConanFile):
    name = "Boost.Level14Group"
    version = "1.65.1"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-level14group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["bimap", "disjoint_sets", "graph", "graph_parallel", "mpi", "property_map"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    build_requires = "Boost.Generator/1.65.1@bincrafters/stable"
    requires = "Boost.Algorithm/1.65.1@bincrafters/stable", \
        "Boost.Any/1.65.1@bincrafters/stable", \
        "Boost.Array/1.65.1@bincrafters/stable", \
        "Boost.Assert/1.65.1@bincrafters/stable", \
        "Boost.Bind/1.65.1@bincrafters/stable", \
        "Boost.Concept_Check/1.65.1@bincrafters/stable", \
        "Boost.Config/1.65.1@bincrafters/stable", \
        "Boost.Conversion/1.65.1@bincrafters/stable", \
        "Boost.Core/1.65.1@bincrafters/stable", \
        "Boost.Detail/1.65.1@bincrafters/stable", \
        "Boost.Dynamic_Bitset/1.65.1@bincrafters/stable", \
        "Boost.Exception/1.65.1@bincrafters/stable", \
        "Boost.Filesystem/1.65.1@bincrafters/stable", \
        "Boost.Foreach/1.65.1@bincrafters/stable", \
        "Boost.Function/1.65.1@bincrafters/stable", \
        "Boost.Functional/1.65.1@bincrafters/stable", \
        "Boost.Integer/1.65.1@bincrafters/stable", \
        "Boost.Iterator/1.65.1@bincrafters/stable", \
        "Boost.Lambda/1.65.1@bincrafters/stable", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/stable", \
        "Boost.Math/1.65.1@bincrafters/stable", \
        "Boost.Move/1.65.1@bincrafters/stable", \
        "Boost.Mpl/1.65.1@bincrafters/stable", \
        "Boost.Multi_Index/1.65.1@bincrafters/stable", \
        "Boost.Optional/1.65.1@bincrafters/stable", \
        "Boost.Parameter/1.65.1@bincrafters/stable", \
        "Boost.Preprocessor/1.65.1@bincrafters/stable", \
        "Boost.Property_Tree/1.65.1@bincrafters/stable", \
        "Boost.Python/1.65.1@bincrafters/stable", \
        "Boost.Random/1.65.1@bincrafters/stable", \
        "Boost.Range/1.65.1@bincrafters/stable", \
        "Boost.Regex/1.65.1@bincrafters/stable", \
        "Boost.Serialization/1.65.1@bincrafters/stable", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
        "Boost.Spirit/1.65.1@bincrafters/stable", \
        "Boost.Static_Assert/1.65.1@bincrafters/stable", \
        "Boost.System/1.65.1@bincrafters/stable", \
        "Boost.Test/1.65.1@bincrafters/stable", \
        "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
        "Boost.Tti/1.65.1@bincrafters/stable", \
        "Boost.Tuple/1.65.1@bincrafters/stable", \
        "Boost.Type_Traits/1.65.1@bincrafters/stable", \
        "Boost.Type_Traits/1.65.1@bincrafters/stable", \
        "Boost.Typeof/1.65.1@bincrafters/stable", \
        "Boost.Unordered/1.65.1@bincrafters/stable", \
        "Boost.Utility/1.65.1@bincrafters/stable", \
        "Boost.Variant/1.65.1@bincrafters/stable", \
        "Boost.Xpressive/1.65.1@bincrafters/stable"

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
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        self.copy(pattern="*", dst="lib", src="stage/lib")
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_info(self):
        self.user_info.lib_short_names = ",".join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")

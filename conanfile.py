from conans import ConanFile, tools, os


class BoostLevel14GroupConan(ConanFile):
    name = "Boost.Level14Group"
    version = "1.64.0"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-level14group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["bimap", "disjoint_sets", "graph", "graph_parallel", "mpi", "property_map"]
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing"
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
        "Boost.Regex/1.64.0@bincrafters/testing", \
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
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name))
               
    def build(self):
        boost_build = self.deps_cpp_info["Boost.Build"]
        b2_bin_name = "b2.exe" if self.settings.os == "Windows" else "b2"
        b2_bin_dir_name = boost_build.bindirs[0]
        b2_full_path = os.path.join(boost_build.rootpath, b2_bin_dir_name, b2_bin_name)
        
        self.run(b2_full_path + " -j4 -a --hash=yes")
        
    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

        self.copy(pattern="*", dst="lib", src="stage/lib")
        
    def package_info(self):
        self.user_info.lib_short_names = (",").join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
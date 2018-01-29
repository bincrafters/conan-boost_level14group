#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel14GroupConan(ConanFile):
    name = "boost_level14group"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_level14group"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = [
        "bimap", "disjoint_sets", "graph", "graph_parallel", "mpi",
        "property_map"]
        
    is_cycle_group = True
    is_header_only = {
        "bimap":True,
        "disjoint_sets":True,
        "graph":False,
        "graph_parallel":False,
        "mpi":False,
        "property_map":True
        }

    options = {"shared": [True, False], "mpicc": "ANY"}
    default_options = "shared=False", "mpicc=default"

    requires = (
        "boost_package_tools/1.66.0@bincrafters/stable",
        "boost_algorithm/1.66.0@bincrafters/stable",
        "boost_any/1.66.0@bincrafters/stable",
        "boost_array/1.66.0@bincrafters/stable",
        "boost_assert/1.66.0@bincrafters/stable",
        "boost_bind/1.66.0@bincrafters/stable",
        "boost_concept_check/1.66.0@bincrafters/stable",
        "boost_config/1.66.0@bincrafters/stable",
        "boost_conversion/1.66.0@bincrafters/stable",
        "boost_core/1.66.0@bincrafters/stable",
        "boost_detail/1.66.0@bincrafters/stable",
        "boost_dynamic_bitset/1.66.0@bincrafters/stable",
        "boost_exception/1.66.0@bincrafters/stable",
        "boost_filesystem/1.66.0@bincrafters/stable",
        "boost_foreach/1.66.0@bincrafters/stable",
        "boost_function/1.66.0@bincrafters/stable",
        "boost_functional/1.66.0@bincrafters/stable",
        "boost_integer/1.66.0@bincrafters/stable",
        "boost_iterator/1.66.0@bincrafters/stable",
        "boost_lambda/1.66.0@bincrafters/stable",
        "boost_lexical_cast/1.66.0@bincrafters/stable",
        "boost_math/1.66.0@bincrafters/stable",
        "boost_move/1.66.0@bincrafters/stable",
        "boost_mpl/1.66.0@bincrafters/stable",
        "boost_multi_index/1.66.0@bincrafters/stable",
        "boost_optional/1.66.0@bincrafters/stable",
        "boost_parameter/1.66.0@bincrafters/stable",
        "boost_preprocessor/1.66.0@bincrafters/stable",
        "boost_property_tree/1.66.0@bincrafters/stable",
        "boost_python/1.66.0@bincrafters/stable",
        "boost_random/1.66.0@bincrafters/stable",
        "boost_range/1.66.0@bincrafters/stable",
        "boost_regex/1.66.0@bincrafters/stable",
        "boost_serialization/1.66.0@bincrafters/stable",
        "boost_smart_ptr/1.66.0@bincrafters/stable",
        "boost_spirit/1.66.0@bincrafters/stable",
        "boost_static_assert/1.66.0@bincrafters/stable",
        "boost_system/1.66.0@bincrafters/stable",
        "boost_test/1.66.0@bincrafters/stable",
        "boost_throw_exception/1.66.0@bincrafters/stable",
        "boost_tti/1.66.0@bincrafters/stable",
        "boost_tuple/1.66.0@bincrafters/stable",
        "boost_type_traits/1.66.0@bincrafters/stable",
        "boost_type_traits/1.66.0@bincrafters/stable",
        "boost_typeof/1.66.0@bincrafters/stable",
        "boost_unordered/1.66.0@bincrafters/stable",
        "boost_utility/1.66.0@bincrafters/stable",
        "boost_variant/1.66.0@bincrafters/stable",
        "boost_xpressive/1.66.0@bincrafters/stable"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.66.0@bincrafters/stable"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLevel14GroupConan(ConanFile):
    # This is now Level 18
    name = "boost_level14group"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    is_cycle_group = True
    lib_short_names = [
        "bimap", "disjoint_sets", "graph", "graph_parallel", "mpi",
        "property_map"]

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
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_algorithm/1.67.0@bincrafters/testing",
        "boost_any/1.67.0@bincrafters/testing",
        "boost_array/1.67.0@bincrafters/testing",
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_bind/1.67.0@bincrafters/testing",
        "boost_concept_check/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_container_hash/1.67.0@bincrafters/testing",
        "boost_conversion/1.67.0@bincrafters/testing",
        "boost_core/1.67.0@bincrafters/testing",
        "boost_detail/1.67.0@bincrafters/testing",
        "boost_dynamic_bitset/1.67.0@bincrafters/testing",
        "boost_filesystem/1.67.0@bincrafters/testing",
        "boost_foreach/1.67.0@bincrafters/testing",
        "boost_function/1.67.0@bincrafters/testing",
        "boost_integer/1.67.0@bincrafters/testing",
        "boost_iterator/1.67.0@bincrafters/testing",
        "boost_lambda/1.67.0@bincrafters/testing",
        "boost_lexical_cast/1.67.0@bincrafters/testing",
        "boost_math/1.67.0@bincrafters/testing",
        "boost_move/1.67.0@bincrafters/testing",
        "boost_mpl/1.67.0@bincrafters/testing",
        "boost_multi_index/1.67.0@bincrafters/testing",
        "boost_optional/1.67.0@bincrafters/testing",
        "boost_parameter/1.67.0@bincrafters/testing",
        "boost_preprocessor/1.67.0@bincrafters/testing",
        "boost_property_tree/1.67.0@bincrafters/testing",
        "boost_python/1.67.0@bincrafters/testing",
        "boost_random/1.67.0@bincrafters/testing",
        "boost_range/1.67.0@bincrafters/testing",
        "boost_serialization/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_spirit/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_test/1.67.0@bincrafters/testing",
        "boost_throw_exception/1.67.0@bincrafters/testing",
        "boost_tti/1.67.0@bincrafters/testing",
        "boost_tuple/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing",
        "boost_typeof/1.67.0@bincrafters/testing",
        "boost_unordered/1.67.0@bincrafters/testing",
        "boost_utility/1.67.0@bincrafters/testing",
        "boost_variant/1.67.0@bincrafters/testing",
        "boost_xpressive/1.67.0@bincrafters/testing"
    )

    #def build_requirements(self):
    #    self.build_requires("python_dev_config/0.3@bincrafters/stable")

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    #def b2_options(self, lib_name=None):
    #    return " --without-mpi"

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_level14group"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

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

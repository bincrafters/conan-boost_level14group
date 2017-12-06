from conans import ConanFile, tools


class BoostLevel14GroupConan(ConanFile):
    name = "Boost.Level14Group"
    version = "1.65.1"

    options = {"shared": [True, False], "mpicc": "ANY"}
    default_options = "shared=False", "mpicc=default"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Algorithm/1.65.1@bincrafters/testing", \
        "Boost.Any/1.65.1@bincrafters/testing", \
        "Boost.Array/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Bind/1.65.1@bincrafters/testing", \
        "Boost.Concept_Check/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Conversion/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Dynamic_Bitset/1.65.1@bincrafters/testing", \
        "Boost.Exception/1.65.1@bincrafters/testing", \
        "Boost.Filesystem/1.65.1@bincrafters/testing", \
        "Boost.Foreach/1.65.1@bincrafters/testing", \
        "Boost.Function/1.65.1@bincrafters/testing", \
        "Boost.Functional/1.65.1@bincrafters/testing", \
        "Boost.Integer/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Lambda/1.65.1@bincrafters/testing", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/testing", \
        "Boost.Math/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Multi_Index/1.65.1@bincrafters/testing", \
        "Boost.Optional/1.65.1@bincrafters/testing", \
        "Boost.Parameter/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Property_Tree/1.65.1@bincrafters/testing", \
        "Boost.Python/1.65.1@bincrafters/testing", \
        "Boost.Random/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.Regex/1.65.1@bincrafters/testing", \
        "Boost.Serialization/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Spirit/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.System/1.65.1@bincrafters/testing", \
        "Boost.Test/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Tti/1.65.1@bincrafters/testing", \
        "Boost.Tuple/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Typeof/1.65.1@bincrafters/testing", \
        "Boost.Unordered/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing", \
        "Boost.Variant/1.65.1@bincrafters/testing", \
        "Boost.Xpressive/1.65.1@bincrafters/testing"

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
    is_cycle_group = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-level14group"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
